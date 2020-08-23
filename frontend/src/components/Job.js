import React from "react";

function Job({ title, description, location, date }) {
  return (
    <div>
      <h2>{title}</h2>
      <p>{description}</p>
    </div>
  );
}

export default Job;
