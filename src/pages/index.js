import React from "react";
import { graphql } from "gatsby";

export default function Template({ data }) {
  const { html } = data.file.childMarkdownRemark;
  return (
    <div className="main">
      <div className="content" dangerouslySetInnerHTML={{ __html: html }} />
    </div>
  );
}

export const pageQuery = graphql`
  query {
    file(base: { eq: "README.md" }) {
      childMarkdownRemark {
        html
      }
    }
  }
`;
