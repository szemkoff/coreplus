import type {SidebarsConfig} from '@docusaurus/types';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    'technical-specs',
    'panels',
    'modules',
    'connections',
    'technical-drawings',
    {
      type: 'category',
      label: 'Tutorial - Extras',
      items: [
        'tutorial-extras/translate-your-site',
        'tutorial-extras/manage-docs-versions',
      ],
    },
  ],
};

export default sidebars;
