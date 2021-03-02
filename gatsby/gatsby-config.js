/**
 * Configure your Gatsby site with this file.
 *
 * See: https://www.gatsbyjs.com/docs/gatsby-config/
 */

module.exports = {
  /* Your site config here */
  plugins: [
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `readme`,
        path: `${__dirname}/../README.md`,
      },
    },
    `gatsby-transformer-remark`,
  ],
};
