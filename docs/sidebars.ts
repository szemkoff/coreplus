import type {Sidebars} from '@docusaurus/plugin-content-docs/src/sidebars/types';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: Sidebars = {
  tutorialSidebar: [
    {type: 'doc', id: 'intro'},
    {type: 'doc', id: 'technical-specs'},
    {type: 'doc', id: 'panels'},
    {type: 'doc', id: 'modules'},
    {type: 'doc', id: 'connections'},
    {type: 'doc', id: 'technical-drawings'},
    {type: 'doc', id: 'plans'},
    {type: 'doc', id: 'assembly-guide'},
  ],
};

export default sidebars;
