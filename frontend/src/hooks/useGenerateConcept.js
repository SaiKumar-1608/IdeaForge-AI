import { useState } from "react";
import { generateConceptsAPI } from "../services/api";

/**
 * Custom hook to generate creative concepts
 */
function useGenerateConcept() {
  const [concepts, setConcepts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const generateConcepts = async (payload) => {
    setLoading(true);
    setError(null);
    // ❌ Do NOT clear concepts here (skeleton handles loading UI)

    try {
      const result = await generateConceptsAPI(payload);
      setConcepts(result);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return {
    generateConcepts,
    concepts,
    loading,
    error,
  };
}

export default useGenerateConcept;
