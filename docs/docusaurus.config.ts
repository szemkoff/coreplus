import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Core+ Modular Construction',
  tagline: 'Advanced Panelized Construction System',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://stantheman.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/House_Construction_Estimate/',

  // GitHub pages deployment config
  organizationName: 'stantheman',
  projectName: 'House_Construction_Estimate',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/stantheman/House_Construction_Estimate/tree/main/docs/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/social-card.jpg',
    navbar: {
      title: 'Core+',
      logo: {
        alt: 'Core+ Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documentation',
        },
        {
          to: '/product-catalog',
          label: 'Product Catalog',
          position: 'left'
        },
        {
          to: '/cost-calculator',
          label: 'Cost Calculator',
          position: 'left'
        },
        {
          to: '/assembly-guide',
          label: 'Assembly Guide',
          position: 'left'
        },
        {
          href: 'https://github.com/stantheman/House_Construction_Estimate',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
            {
              label: 'Technical Specifications',
              to: '/docs/technical-specs',
            },
            {
              label: 'Assembly Guide',
              to: '/docs/assembly-guide',
            },
          ],
        },
        {
          title: 'Products',
          items: [
            {
              label: 'Panel Systems',
              to: '/docs/panels',
            },
            {
              label: 'Connection Systems',
              to: '/docs/connections',
            },
            {
              label: 'Complete Modules',
              to: '/docs/modules',
            },
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: 'Cost Calculator',
              to: '/cost-calculator',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/stantheman/House_Construction_Estimate',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Core+ Modular Construction.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
