import React, { useState } from "react";
import ConceptList from "../components/concept/ConceptList";
import ErrorAlert from "../components/common/ErrorAlert";
import Button from "../components/common/Button";
import Input from "../components/common/Input";
import TextArea from "../components/common/TextArea";
import useGenerateConcept from "../hooks/useGenerateConcept";
import ConceptSkeleton from "../components/ConceptSkeleton";

function GenerateConcept() {
  const [formData, setFormData] = useState({
    product: "",
    objective: "",
    audience: "",
    tone: "",
    keywords: "",
  });

  // 🔁 Store last successful request (for Regenerate)
  const [lastRequest, setLastRequest] = useState(null);

  // ✅ Concept selection (future-proof)
  const [selectedIndex, setSelectedIndex] = useState(null);

  const {
    generateConcepts,
    concepts,
    loading,
    error,
  } = useGenerateConcept();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (loading) return;

    const payload = { ...formData };

    setLastRequest(payload);
    setSelectedIndex(null); // reset selection
    await generateConcepts(payload);
  };

  const handleRegenerate = async () => {
    if (!lastRequest || loading) return;

    setSelectedIndex(null); // reset selection
    await generateConcepts(lastRequest);
  };

  return (
    <div>
      <h2 style={{ fontSize: "24px", marginBottom: "16px" }}>
        Concept-to-Creative Ideation
      </h2>

      <p style={{ marginBottom: "24px", color: "#555" }}>
        Fill in the campaign brief to generate creative advertising concepts.
      </p>

      {/* ----------- FORM ----------- */}
      <form onSubmit={handleSubmit} style={{ marginBottom: "32px" }}>
        <Input
          label="Product"
          name="product"
          value={formData.product}
          onChange={handleChange}
          placeholder="e.g. Orange Juice"
          required
          disabled={loading}
        />

        <TextArea
          label="Campaign Objective"
          name="objective"
          value={formData.objective}
          onChange={handleChange}
          placeholder="e.g. Promote healthy morning habits"
          required
          disabled={loading}
        />

        <Input
          label="Target Audience"
          name="audience"
          value={formData.audience}
          onChange={handleChange}
          placeholder="e.g. Families"
          required
          disabled={loading}
        />

        <Input
          label="Brand Tone"
          name="tone"
          value={formData.tone}
          onChange={handleChange}
          placeholder="e.g. Fresh, Energetic"
          required
          disabled={loading}
        />

        <Input
          label="Keywords (optional)"
          name="keywords"
          value={formData.keywords}
          onChange={handleChange}
          placeholder="e.g. morning, energy, natural"
          disabled={loading}
        />

        <div style={{ marginTop: "20px", display: "flex", gap: "12px" }}>
          <Button type="submit" disabled={loading}>
            {loading ? "Generating..." : "Generate Concepts"}
          </Button>

          {/* 🔄 Regenerate Button */}
          <Button
            type="button"
            onClick={handleRegenerate}
            disabled={loading || !lastRequest}
          >
            🔄 Regenerate
          </Button>
        </div>
      </form>

      {/* ----------- ERROR ----------- */}
      {error && <ErrorAlert message={error} />}

      {/* ----------- LOADING (Skeletons) ----------- */}
      {loading && <ConceptSkeleton count={3} />}

      {/* ----------- RESULTS ----------- */}
      {!loading && concepts && concepts.length > 0 && (
        <ConceptList
          concepts={concepts}
          selectedIndex={selectedIndex}
          onSelect={setSelectedIndex}
        />
      )}
    </div>
  );
}

export default GenerateConcept;
