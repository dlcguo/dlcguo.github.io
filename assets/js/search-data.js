// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "a collection of projects that I&#39;ve worked on",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "github infographic",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-paper-summaries",
          title: "paper summaries",
          description: "summaries of papers I&#39;ve read",
          section: "Navigation",
          handler: () => {
            window.location.href = "/summaries/";
          },
        },{id: "nav-cmu-course-reviews",
          title: "cmu course reviews",
          description: "a collection of thoughts on courses taken",
          section: "Navigation",
          handler: () => {
            window.location.href = "/courses/";
          },
        },{id: "post-compiler-design-course-experience-cmu",
      
        title: "Compiler Design Course Experience @ CMU",
      
      description: "This is a reflection on my experience with the Compiler Design course (15-411) at CMU. It covers general course thoughts, what I enjoyed the most, and my personal takeaways. For context, 15-411 covers the design and implementation of compiler and runtime systems for high-level languages. Topics include lexical and syntactic analysis, type-checking, program analysis, code generation and optimization, memory management, and runtime organization. The course focuses on developing an end-to-end compiler pipeline for C0 (CMU&#39;s memory-safe C subset).",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2025/compiler-design-course-experience-cmu/";
        
      },
    },{id: "news-fasdf",
          title: 'fasdf',
          description: "",
          section: "News",},{id: "news-",
          title: '',
          description: "",
          section: "News",},{id: "projects-lucas-kanade-video-tracking",
          title: 'Lucas-Kanade Video Tracking',
          description: "an implementation of 3 basic tracking algorithms",
          section: "Projects",handler: () => {
              window.location.href = "/projects/lk_project/";
            },},{id: "projects-neural-nets-for-recognition",
          title: 'Neural Nets for Recognition',
          description: "a neural network from ground-up to recognize characters",
          section: "Projects",handler: () => {
              window.location.href = "/projects/nn_project/";
            },},{id: "summaries-freetimegs-free-gaussian-primitives-at-anytime-and-anywhere-for-dynamic-scene-reconstruction",
          title: 'FreeTimeGS: Free Gaussian Primitives at Anytime and Anywhere for Dynamic Scene Reconstruction',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2025-06-09-freetimegs-free-gaussian-primitives-at-anytime-and-anywhere-for-dynamic-scene-reconstruction/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%64%67%75%6F%33@%63%73.%63%6D%75.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/dlcguo", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },];
