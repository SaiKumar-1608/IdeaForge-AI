import React from "react";
import ConceptCard from "./ConceptCard";

function ConceptList({ concepts, selectedIndex, onSelect }) {
  return (
    <div>
      {concepts.map((concept, index) => (
        <ConceptCard
          key={index}
          concept={concept}
          isSelected={selectedIndex === index}
          onSelect={() => onSelect(index)}
        />
      ))}
    </div>
  );
}

export default ConceptList;
