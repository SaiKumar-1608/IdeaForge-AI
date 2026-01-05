// Centralized API service for IdeaForge AI (Production-grade)

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

const API_PREFIX = "/api";
const API_VERSION = "v1";

// ⏱ Request timeout (milliseconds)
const REQUEST_TIMEOUT = 15000;

/**
 * Normalize backend HTTP errors into UX-friendly errors
 */
async function handleApiResponse(response) {
  if (response.ok) {
    return response.json();
  }

  let backendMessage = "Something went wrong.";

  try {
    const errorData = await response.json();
    backendMessage = errorData.detail || backendMessage;
  } catch {
    // Ignore JSON parsing errors
  }

  switch (response.status) {
    case 400:
      throw {
        type: "VALIDATION_ERROR",
        message:
          backendMessage ||
          "Your input contains restricted or invalid content. Please revise it."
      };

    case 429:
      throw {
        type: "RATE_LIMIT_ERROR",
        message:
          "You are making requests too frequently. Please wait a moment and try again."
      };

    case 500:
      throw {
        type: "SERVER_ERROR",
        message:
          "An internal error occurred while generating concepts. Please try again later."
      };

    default:
      throw {
        type: "UNKNOWN_ERROR",
        message: backendMessage
      };
  }
}

/**
 * Perform fetch with timeout protection
 */
async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal
    });

    return response;
  } catch (error) {
    // ⏱ Timeout error
    if (error.name === "AbortError") {
      throw {
        type: "TIMEOUT_ERROR",
        message:
          "The request took too long to respond. Please check your connection and try again."
      };
    }

    // 🌐 Network / CORS / unreachable backend
    throw {
      type: "NETWORK_ERROR",
      message:
        "Unable to reach the server. Please check your connection and try again."
    };
  } finally {
    clearTimeout(timeoutId);
  }
}

/**
 * Generate creative concepts from backend
 * @param {Object} payload - Creative brief data
 * @returns {Promise<Array>} - List of generated concepts
 */
export async function generateConceptsAPI(payload) {
  try {
    const response = await fetchWithTimeout(
      `${API_BASE_URL}${API_PREFIX}/${API_VERSION}/generate-concepts`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      }
    );

    const data = await handleApiResponse(response);

    // Expected backend shape: { success: true, concepts: [...] }
    return data.concepts || [];

  } catch (error) {
    // Already-normalized error
    if (error.type) {
      throw error;
    }

    // Fallback safety
    throw {
      type: "UNKNOWN_ERROR",
      message: "An unexpected error occurred. Please try again."
    };
  }
}
