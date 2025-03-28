"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[867],{1865:(e,t,a)=>{a.d(t,{A:()=>l});a(6540);var s=a(4164),n=a(6289),r=a(4848);function l(e){const{permalink:t,title:a,subLabel:l,isNext:i}=e;return(0,r.jsxs)(n.A,{className:(0,s.A)("pagination-nav__link",i?"pagination-nav__link--next":"pagination-nav__link--prev"),to:t,children:[l&&(0,r.jsx)("div",{className:"pagination-nav__sublabel",children:l}),(0,r.jsx)("div",{className:"pagination-nav__label",children:a})]})}},6547:(e,t,a)=>{a.d(t,{A:()=>d});a(6540);var s=a(4164),n=a(539),r=a(6289);const l={tag:"tag_zVej",tagRegular:"tagRegular_sFm0",tagWithCount:"tagWithCount_h2kH"};var i=a(4848);function o(e){let{permalink:t,label:a,count:n,description:o}=e;return(0,i.jsxs)(r.A,{href:t,title:o,className:(0,s.A)(l.tag,n?l.tagWithCount:l.tagRegular),children:[a,n&&(0,i.jsx)("span",{children:n})]})}const c={tags:"tags_jXut",tag:"tag_QGVx"};function d(e){let{tags:t}=e;return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)("b",{children:(0,i.jsx)(n.A,{id:"theme.tags.tagsListLabel",description:"The label alongside a tag list",children:"Tags:"})}),(0,i.jsx)("ul",{className:(0,s.A)(c.tags,"padding--none","margin-left--sm"),children:t.map((e=>(0,i.jsx)("li",{className:c.tag,children:(0,i.jsx)(o,{...e})},e.permalink)))})]})}},9330:(e,t,a)=>{a.r(t),a.d(t,{default:()=>V});a(6540);var s=a(4164),n=a(1082),r=a(204),l=a(1926),i=a(6289),o=a(3750),c=a(569),d=a(539),g=a(1865),m=a(4848);function u(e){const{metadata:t}=e,{previousPage:a,nextPage:s}=t;return(0,m.jsxs)("nav",{className:"pagination-nav","aria-label":(0,d.T)({id:"theme.blog.paginator.navAriaLabel",message:"Blog list page navigation",description:"The ARIA label for the blog pagination"}),children:[a&&(0,m.jsx)(g.A,{permalink:a,title:(0,m.jsx)(d.A,{id:"theme.blog.paginator.newerEntries",description:"The label used to navigate to the newer blog posts page (previous page)",children:"Newer entries"})}),s&&(0,m.jsx)(g.A,{permalink:s,title:(0,m.jsx)(d.A,{id:"theme.blog.paginator.olderEntries",description:"The label used to navigate to the older blog posts page (next page)",children:"Older entries"}),isNext:!0})]})}var h=a(7220);function x(e){let{children:t,className:a}=e;return(0,m.jsx)("article",{className:a,children:t})}const j="title_f1Hy";function p(e){let{className:t}=e;const{metadata:a,isBlogPostPage:n}=(0,o.e7)(),{permalink:r,title:l}=a,c=n?"h1":"h2";return(0,m.jsx)(c,{className:(0,s.A)(j,t),children:n?l:(0,m.jsx)(i.A,{to:r,children:l})})}var b=a(1430),f=a(8569);const A="container_mt6G";function v(e){let{readingTime:t}=e;const a=function(){const{selectMessage:e}=(0,b.W)();return t=>{const a=Math.ceil(t);return e(a,(0,d.T)({id:"theme.blog.post.readingTime.plurals",description:'Pluralized label for "{readingTime} min read". Use as much plural forms (separated by "|") as your language support (see https://www.unicode.org/cldr/cldr-aux/charts/34/supplemental/language_plural_rules.html)',message:"One min read|{readingTime} min read"},{readingTime:a}))}}();return(0,m.jsx)(m.Fragment,{children:a(t)})}function N(e){let{date:t,formattedDate:a}=e;return(0,m.jsx)("time",{dateTime:t,children:a})}function _(){return(0,m.jsx)(m.Fragment,{children:" \xb7 "})}function T(e){let{className:t}=e;const{metadata:a}=(0,o.e7)(),{date:n,readingTime:r}=a,l=(0,f.i)({day:"numeric",month:"long",year:"numeric",timeZone:"UTC"});return(0,m.jsxs)("div",{className:(0,s.A)(A,"margin-vert--md",t),children:[(0,m.jsx)(N,{date:n,formattedDate:(i=n,l.format(new Date(i)))}),void 0!==r&&(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(_,{}),(0,m.jsx)(v,{readingTime:r})]})]});var i}var k=a(5921);const w="authorCol_Hf19",P="imageOnlyAuthorRow_pa_O",R="imageOnlyAuthorCol_G86a";function U(e){let{className:t}=e;const{metadata:{authors:a},assets:n}=(0,o.e7)();if(0===a.length)return null;const r=a.every((e=>{let{name:t}=e;return!t})),l=1===a.length;return(0,m.jsx)("div",{className:(0,s.A)("margin-top--md margin-bottom--sm",r?P:"row",t),children:a.map(((e,t)=>(0,m.jsx)("div",{className:(0,s.A)(!r&&(l?"col col--12":"col col--6"),r?R:w),children:(0,m.jsx)(k.A,{author:{...e,imageURL:n.authorsImageUrls[t]??e.imageURL}})},t)))})}function y(){return(0,m.jsxs)("header",{children:[(0,m.jsx)(p,{}),(0,m.jsx)(T,{}),(0,m.jsx)(U,{})]})}var F=a(99),L=a(4522);function C(e){let{children:t,className:a}=e;const{isBlogPostPage:n}=(0,o.e7)();return(0,m.jsx)("div",{id:n?F.LU:void 0,className:(0,s.A)("markdown",a),children:(0,m.jsx)(L.A,{children:t})})}var M=a(5783),B=a(6547);function G(){return(0,m.jsx)("b",{children:(0,m.jsx)(d.A,{id:"theme.blog.post.readMore",description:"The label used in blog post item excerpts to link to full blog posts",children:"Read more"})})}function O(e){const{blogPostTitle:t,...a}=e;return(0,m.jsx)(i.A,{"aria-label":(0,d.T)({message:"Read more about {title}",id:"theme.blog.post.readMoreLabel",description:"The ARIA label for the link to full blog posts from excerpts"},{title:t}),...a,children:(0,m.jsx)(G,{})})}function E(){const{metadata:e,isBlogPostPage:t}=(0,o.e7)(),{tags:a,title:n,editUrl:l,hasTruncateMarker:i,lastUpdatedBy:c,lastUpdatedAt:d}=e,g=!t&&i,u=a.length>0;if(!(u||g||l))return null;if(t){const e=!!(l||d||c);return(0,m.jsxs)("footer",{className:"docusaurus-mt-lg",children:[u&&(0,m.jsx)("div",{className:(0,s.A)("row","margin-top--sm",r.G.blog.blogFooterEditMetaRow),children:(0,m.jsx)("div",{className:"col",children:(0,m.jsx)(B.A,{tags:a})})}),e&&(0,m.jsx)(M.A,{className:(0,s.A)("margin-top--sm",r.G.blog.blogFooterEditMetaRow),editUrl:l,lastUpdatedAt:d,lastUpdatedBy:c})]})}return(0,m.jsxs)("footer",{className:"row docusaurus-mt-lg",children:[u&&(0,m.jsx)("div",{className:(0,s.A)("col",{"col--9":g}),children:(0,m.jsx)(B.A,{tags:a})}),g&&(0,m.jsx)("div",{className:(0,s.A)("col text--right",{"col--3":u}),children:(0,m.jsx)(O,{blogPostTitle:n,to:e.permalink})})]})}function I(e){let{children:t,className:a}=e;const n=function(){const{isBlogPostPage:e}=(0,o.e7)();return e?void 0:"margin-bottom--xl"}();return(0,m.jsxs)(x,{className:(0,s.A)(n,a),children:[(0,m.jsx)(y,{}),(0,m.jsx)(C,{children:t}),(0,m.jsx)(E,{})]})}function W(e){let{items:t,component:a=I}=e;return(0,m.jsx)(m.Fragment,{children:t.map((e=>{let{content:t}=e;return(0,m.jsx)(o.in,{content:t,children:(0,m.jsx)(a,{children:(0,m.jsx)(t,{})})},t.metadata.permalink)}))})}function D(e){let{author:t}=e;const a=(0,l.wI)(t);return(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(n.be,{title:a}),(0,m.jsx)(h.A,{tag:"blog_authors_posts"})]})}function H(){const{authorsListPath:e}=(0,o.x)();return(0,m.jsx)(i.A,{href:e,children:(0,m.jsx)(l.np,{})})}function z(e){let{author:t,items:a,sidebar:s,listMetadata:n}=e;return(0,m.jsxs)(c.A,{sidebar:s,children:[(0,m.jsxs)("header",{className:"margin-bottom--xl",children:[(0,m.jsx)(k.A,{as:"h1",author:t}),t.description&&(0,m.jsx)("p",{children:t.description}),(0,m.jsx)(H,{})]}),0===a.length?(0,m.jsx)("p",{children:(0,m.jsx)(l.Y4,{})}):(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)("hr",{}),(0,m.jsx)(W,{items:a}),(0,m.jsx)(u,{metadata:n})]})]})}function V(e){return(0,m.jsxs)(n.e3,{className:(0,s.A)(r.G.wrapper.blogPages,r.G.page.blogAuthorsPostsPage),children:[(0,m.jsx)(D,{...e}),(0,m.jsx)(z,{...e})]})}}}]);