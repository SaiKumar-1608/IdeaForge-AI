/**
 * Basic frontend validation utilities
 * Backend validation is the source of truth
 */

/**
 * Check if required fields are filled
 * @param {Object} data
 * @returns {string|null} error message or null
 */
export function validateRequiredFields(data) {
  const requiredFields = ["product", "objective", "audience", "tone"];

  for (const field of requiredFields) {
    if (!data[field] || data[field].trim() === "") {
      return `Please fill in the ${field} field.`;
    }
  }

  return null;
}

/**
 * Prevent extremely long input (UX protection only)
 * @param {string} text
 * @param {number} maxLength
 * @returns {boolean}
 */
export function exceedsMaxLength(text, maxLength = 500) {
  if (!text) return false;
  return text.length > maxLength;
}

/**
 * Lightweight validator before submit
 * @param {Object} formData
 * @returns {string|null}
 */
export function validateForm(formData) {
  const requiredError = validateRequiredFields(formData);
  if (requiredError) return requiredError;

  if (exceedsMaxLength(formData.objective, 500)) {
    return "Campaign objective is too long (max 500 characters).";
  }

  if (exceedsMaxLength(formData.audience, 300)) {
    return "Audience description is too long (max 300 characters).";
  }

  return null;
}
