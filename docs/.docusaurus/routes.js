import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/coreplus/assembly-guide',
    component: ComponentCreator('/coreplus/assembly-guide', '3fb'),
    exact: true
  },
  {
    path: '/coreplus/blog/authors',
    component: ComponentCreator('/coreplus/blog/authors', 'baf'),
    exact: true
  },
  {
    path: '/coreplus/blog/authors/all-sebastien-lorber-articles',
    component: ComponentCreator('/coreplus/blog/authors/all-sebastien-lorber-articles', 'c22'),
    exact: true
  },
  {
    path: '/coreplus/blog/authors/yangshun',
    component: ComponentCreator('/coreplus/blog/authors/yangshun', '948'),
    exact: true
  },
  {
    path: '/coreplus/contact',
    component: ComponentCreator('/coreplus/contact', '782'),
    exact: true
  },
  {
    path: '/coreplus/cost-calculator',
    component: ComponentCreator('/coreplus/cost-calculator', 'f1d'),
    exact: true
  },
  {
    path: '/coreplus/markdown-page',
    component: ComponentCreator('/coreplus/markdown-page', '1fb'),
    exact: true
  },
  {
    path: '/coreplus/product-catalog',
    component: ComponentCreator('/coreplus/product-catalog', '777'),
    exact: true
  },
  {
    path: '/coreplus/docs',
    component: ComponentCreator('/coreplus/docs', '080'),
    routes: [
      {
        path: '/coreplus/docs',
        component: ComponentCreator('/coreplus/docs', '62d'),
        routes: [
          {
            path: '/coreplus/docs',
            component: ComponentCreator('/coreplus/docs', '063'),
            routes: [
              {
                path: '/coreplus/docs/assembly-guide',
                component: ComponentCreator('/coreplus/docs/assembly-guide', '229'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/coreplus/docs/connections',
                component: ComponentCreator('/coreplus/docs/connections', '722'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/coreplus/docs/intro',
                component: ComponentCreator('/coreplus/docs/intro', '31f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/coreplus/docs/modules',
                component: ComponentCreator('/coreplus/docs/modules', 'b45'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/coreplus/docs/panels',
                component: ComponentCreator('/coreplus/docs/panels', 'cf6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/coreplus/docs/technical-specs',
                component: ComponentCreator('/coreplus/docs/technical-specs', '0e3'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/coreplus/',
    component: ComponentCreator('/coreplus/', '6cd'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
