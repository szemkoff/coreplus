import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMermaid from 'mdx-mermaid';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Core+ Modular Construction',
  tagline: 'Advanced Panelized Construction System',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://szemkoff.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/coreplus/',

  // GitHub pages deployment config
  organizationName: 'szemkoff',
  projectName: 'coreplus',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  markdown: {
    mermaid: true,
  },

  themes: ['@docusaurus/theme-mermaid'],

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
          editUrl: 'https://github.com/szemkoff/coreplus/tree/main/docs/',
          remarkPlugins: [remarkMermaid],
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
          to: '/docs/technical-specs',
          label: 'Technical Specs',
          position: 'left'
        },
        {
          to: '/docs/customer-proposal',
          label: 'Customer Proposal',
          position: 'left'
        },
        {
          href: 'https://github.com/szemkoff/coreplus',
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
              label: 'Technical Specifications',
              to: '/docs/technical-specs',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/szemkoff/coreplus',
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
