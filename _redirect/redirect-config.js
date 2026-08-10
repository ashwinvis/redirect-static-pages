// Domain redirect configuration

const REDIRECT_CONFIG = {
  OLD_DOMAIN: 'old.fluid.quest/redirect-static-pages/',
  NEW_DOMAIN: 'example.com',
  PROTOCOL: 'https://'
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = REDIRECT_CONFIG;
}
