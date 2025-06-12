---
layout: page
permalink: /courses/
title: cmu course reviews
description: a collection of thoughts on courses taken
nav: true
nav_order: 5
toc:
  sidebar: left
giscus_comments: true
---

This page is to share my thoughts on courses I have taken at CMU so far.

A &#9733; indicates courses I found most informative, whereas a &hearts; denotes the ones I really enjoyed.

Feel free to email or comment below if you have any questions or spot mistakes on this page.

{% assign n = site.data.course_review_blogs.blogs | size %}
{% assign blogs = site.data.course_review_blogs.blogs | sample: n %}
Below are some other CMU course review pages, in random order every time this site gets built:

{% for blog in blogs %}[&#10070;]({{ blog }}) {% endfor %}

## Categories

The classes have been categorized by domain to make navigation easier.

### Computer Science Theory and Algorithms

| Computer Science Theory and Algorithms                                        |
| ----------------------------------------------------------------------------- |
| [15-251 Great Ideas in Theoretical Computer Science](#course15251)            |
| [15-210 Parallel and Sequential Data Structures and Algorithms](#course15210) |

{: .table .table-bordered .table-hover .table-sm }

<br>

### Machine Learning and Artificial Intelligence

| Machine Learning and Artificial Intelligence                                       |
| ---------------------------------------------------------------------------------- |
| [10-701 Introduction to Machine Learning](#course10701)                            |
| [15-281 Artificial Intelligence: Representation and Problem Solving](#course15281) |

{: .table .table-bordered .table-hover .table-sm }

<br>

### Computer Vision and Robotics

| Computer Vision and Robotics           |
| -------------------------------------- |
| [16-385 Computer Vision](#course16385) |

{: .table .table-bordered .table-hover .table-sm }

<br>

### Computer Systems

| Computer Systems                                        |
| ------------------------------------------------------- |
| [15-411 Compiler Design](#course15411)                  |
| [15-213 Introduction to Computer Systems](#course15213) |

{: .table .table-bordered .table-hover .table-sm }

<br>

### Human-Computer Interaction

| Human-Computer Interaction                  |
| ------------------------------------------- |
| [05-318 Human-AI Interaction](#course05318) |

{: .table .table-bordered .table-hover .table-sm }

<br>

### Mathematics

| Mathematics                                                          |
| -------------------------------------------------------------------- |
| [36-218 Probability Theory for Computer Scientists](#course36218)    |
| [21-266 Vector Calculus for Computer Scientists](#course21266)       |
| [21-241 Matrices and Linear Transformations](#course21241)           |
| [15-151 Mathematical Foundations for Computer Science](#course15151) |

{: .table .table-bordered .table-hover .table-sm }

<br>

### Computer Science - Others

| Computer Science - Others                                        |
| ---------------------------------------------------------------- |
| [15-150 Functional Programming](#course15150)                    |
| [15-122 Principles of Imperative Computation](#course15122)      |
| [07-131 Great Practical Ideas in Computer Science](#course07131) |
| [07-128 First Year Immigration Course](#course07128)             |

{: .table .table-bordered .table-hover .table-sm }

<br>

### General Education and Everything Else

| General Education and Everything Else                                           |
| ------------------------------------------------------------------------------- |
| [85-211 Cognitive Psychology](#course85211)                                     |
| [84-275 Comparative Politics](#course84275)                                     |
| [82-279 Anime - Visual Interplay between Japan and the World](#course82279)     |
| [02-261 Quantitative Cellular and Molecular Biology Laboratory](#course02261)   |
| [03-151 Honors Modern Biology](#course03151)                                    |
| [76-106/76-107 Writing about Literature/Writing about Data](#course76106-76107) |

{: .table .table-bordered .table-hover .table-sm }

---

## CMU Courses

### Spring 2025

{: .first-course-item #course15411 }

- &#9733; 15-411 [**Compiler Design**](https://www.cs.cmu.edu/~15411/), [Seth Goldstein](https://www.cs.cmu.edu/~seth/) and [Ben Titzer](https://s3d.cmu.edu/people/core-faculty/titzer-ben.html)

  There is so much to talk about for this class that I am writing a separate, detailed post for it that you can find [here]({{ "/blog/2025/compiler-design-course-experience-cmu" | relative_url }}); I recommend reading it if you have any interest in the class. TLDR is that there is a HUGE amount of informative and interesting content covered in the class, which also means that it is a tremendous time commitment (I cannot emphasize this point enough). I believe this class in terms of effort is matched or overshadowed only by Operating Systems (15-410).

- &hearts; 10-701 **Introduction to Machine Learning**, [Geoff Gordon](https://www.cs.cmu.edu/~ggordon/) and [Max Simchowitz](https://msimchowitz.github.io/)
  {: .course-item #course10701 }

  This is one of the many options for a student's first intro to machine learning class here; my personal opinion is that this is the best choice aside from 10-715 which requires a strong prior ML/math background. Lectures tended to be quite theoretical, mainly focusing on proofs and theory. Assignments usually had a programming component that focused on implementation details and written components with an emphasis on derivations/proofs and calculations. Exams were reasonable and honestly much easier than the homework. While some basic topics like gradient descent are covered for the ninth gazillion times, a lot of neat things like kernels, PAC learning, and VC dimension have their own lectures which I thought was cool. I will be cautious and note that the course does have numerous faults like pacing which I believe is unavoidable. Being a graduate-level course, there is a lot of variance of students' backgrounds coming into the class; this got further exacerbated by the funny fact that half the class (I kid not) was composed of undergraduate sophomores like me. This makes it incredibly challenging to structure the course to be a level appropriate for everyone. I also think that not many professors want to teach this class for the variance reason as well, given the variance reason, meaning the people teaching this class consistently change between semesters, which doesn't do any favors concerning improving course structure. I do admit that I liked the professors a lot for this semester; they felt somewhat relatable and a lot more down-to-earth after a Q&A session we had near the end of the semester (we asked a bunch of casual questions like their opinions on-campus dining and their daily schedule haha but also questions leaning towards the direction of academic advice). In particular, Max had many takes on what constitutes a good course I also agree with such as course notes detailed enough to provide a comprehensive understanding of lecture content (this class did not have that unfortunately but I'm sure in the future he'll steer whatever classes he ends up teaching in this direction). Given all circumstances, I think the course does a good job of teaching foundations to pursue more specialized domains of machine learning.

- 15-281 [**Artificial Intelligence: Representation and Problem Solving**](https://www.cs.cmu.edu/~15281/), [Tuomas Sandholm](https://www.cs.cmu.edu/~sandholm/) and [Vincent Conitzer](https://www.cs.cmu.edu/~conitzer/)
  {: .course-item #course15281 }

  This class is somewhat infamous for its lack of course structure to the point that it reached the ears of many CS academic advisors. As such, in the coming semesters, this course and the undergraduate intro to machine learning class are being abolished in favor of new, revamped courses. Still, I'll provide some of my thoughts. First off, I don't believe the problems of the course lie in the teaching abilities of the professor, but rather in the disorganized course structure/logistics. There have been many instances of unreasonable or unclear instructions on homework and tests. Aside from that, my personal opinion is that the course fails to fulfill a specific purpose. With the number of topics covered, much of the information from the class is only at the surface level. While it's true that 15-281 is only supposed to be an intro-level class, I feel like this approach, along with how most of the work done is computationally heavy, leaves a weak foundation for subsequent higher-level classes. This is not to mention that topics with weak association to core concepts from the class like AI ethics and game theory get multiple separate lectures which further detract from more in-depth understandings of more important ideas. Adding onto the surface level understanding point, a personal dislike I have about the class is just that because it is essentially just computations, you can succeed in the class just by memorizing steps and not necessarily the rationale behind them. This made the course not difficult, but also not entirely educational. To summarize, I think the course had mostly the right idea in terms of core topics, but poor execution.

  This all said, I will note something I and many other people find really helpful the concise but thorough course notes for core topics. These contained basically enough information to get by the entire course. I think that having something similar to this in the revamped version of this class (and in general all classes) should be non-negotiable.

- 05-318 **Human-AI Interaction**, [Haiyi Zhu](https://haiyizhu.com/) and [Motahhare Eslami](https://hcii.cmu.edu/people/motahhare-eslami)
  {: .course-item #course05318 }

  I don't really have much to say about this class; I mainly took it since it satisfies a requirement and is low-effort. The course is easy in the sense that homework consists of just four short programming assignments and reflections for a Human-Computer Interaction that is covered during every lecture. There is a final project where students have the option to choose between writing a short paper on research/topic of choice and creating an app. Some of the papers we read did end up being pretty interesting like introducing greater transparency and understandability behind the decisions of AI models. One such paper I particularly liked is [this](https://dl.acm.org/doi/pdf/10.1145/2939672.2939778). I guess one unrelated takeaway I got from this class though is that HCI classes are generally much easier than other traditional CS/ML classes.

- 02-261 **Quantitative Cellular and Molecular Biology Laboratory**, [Joshua Kangas](https://cbd.cmu.edu/people/kangas.html)
  {: .course-item #course02261 }

  This course was to fulfill my lab Gen-Ed requirement, and honestly, the only option I wanted to take. Since there aren't many details about the class online, I'll be a bit more detailed with logistics. The grading scheme is organized into participation, homework, and a final project. Generally, homework is not too heavy and is graded pretty leniently, making the class relatively stress-free. Weekly labs and the final project are done in groups of 3-4, which were randomly selected at the beginning of the semester I took the class. The final project was designing an experiment related to things learned during class. The actual content from the class involved incorporating computational analytic methods into traditional laboratory experiments e.g. automating the feature extraction process from bacterial colonies grown on agar plates and implementing pipelines for genome similarity matching after performing PCR. My final thoughts are that I think this class is one of the best options for the lab Gen-Ed requirement in terms of workload and enjoyment, though it is on the harder side of courses to enroll in. I will say that Professor Kangas played a large role in my enjoyment of the class. He was relatively laid-back but still open to discussing random concepts in more detail. Plus, he kind of vibe-checked attendance (mentioned that he wouldn't really count absences unless there is consistently low attendance by the entire class) and got everyone pizza for dinner during the final project presentation. That said, new lab equipment was brought this semester, so it should be easier to take in later on.

Units: 60

This had been my heaviest semester yet, mostly due to compilers. The 15 units assigned to the class do not do justice to its actual time commitment; this course took more time than all my other courses this semester combined. I mentioned a disinterest in systems previously [here](#Systems-Disinterest), though I would not include compiler systems in that group anymore. Without a doubt, debugging had still been a major (frustrating) part of my experience where I had to analyze things like assembly code to find what was wrong. However, I ended up really enjoying the algorithmic aspects of compilers like dataflow analysis, graph structures, and optimizations. Since the project was done in OCaml, a functional language, problems generally boiled down to neat recursive solutions which was satisfying.

Something I realized I need to get better at is distributing how I spend my time on work. This hadn't been so much of an issue previously, but I tend to get fixated on wanting to finish one task before starting the next. This wasn't so much of a noticeable issue before, but it became noticeably problematic when having to work on compilers; I ended up spending a lot of time unproductively, for reasons of either needing to go to office hours later or just not thinking clearly out of frustration.

One thing I experimented with a bit this semester was different forms of note-taking. I wanted to get back into the habit of taking _good_ notes to make the process of reviewing for exams easier. I tried LaTeX, Typst, tablet, and paper notes. My personal findings are that:

1. I think in terms of typeset notes, I definitely prefer Typst of LaTeX. It's generally easier to write and nicer to format, though it comes with the drawback that most of my homework is done in LaTeX so I'm less familiar with Typst.

2. I am not the biggest fan of tablet notes since for me at least, it feels awkward and slower writing on a glass surface than on paper. I don't think I will be doing this often except when I really like a class's notes template or slides (to write on top of).

3. Paper notes are my favorite. There's just something incredibly satisfying about writing with a gel pen.

4. With regard to typed vs. written notes, I think that written notes let me retain things better in the sense that I constrain myself to reorganize lecture content in a concise form that makes sense to me. Still, I definitely prefer typed notes for implementation-heavy classes (that are generally project-based) like compilers for efficiency's sake granted I don't need complete familiarity with specific topics, just enough to know where to investigate further in the scenario I don't have enough information.

In general, I'm quite happy with the upper-div courses I'm starting to have access to since they are (surprise, surprise) a lot more in-depth and specific than the intro classes. Of course, that comes with the added difficulty factor but even then it feels rewarding to overcome challenges. Moving forward, I think I am going to be prioritizing taking more machine learning-focused classes.

### Fall 2024

{: .first-course-item #course15213 }

- 15-213 [**Introduction to Computer Systems**](https://www.cs.cmu.edu/~213/), [Brian Railing](https://www.cs.cmu.edu/~bpr/)

  One of the more often mentioned courses @ CMU. As the name hints, this is CMU's version of what typically is a student's first computer systems course. There is a great surplus of posts detailing the course's content so I won't dive much into specific details. In general, the class covers a lot of topics, which consequently results in much less depth than I would have liked. This is somewhat expected though, given the course's intended purpose of being a foundation for many different systems courses. Still, I would rate the structure of the class highly. There is an abundance of resources for students who need help whether it is office hours, recitation notes, Piazza access, and more; this is in addition to how the course somewhat adheres to the [CS:APP3e textbook](https://csapp.cs.cmu.edu/) (I personally have much better experiences with classes that offer some sort of written notes to follow). I don't think the class is really difficult given the amount of support offered, making it essentially guaranteed to earn perfect scores on labs, granted you put time in. Still, I will say the course covers many useful topics like assembly and memory management important for systems courses.

- 36-218 **Probability Theory for Computer Scientists**, [Chris Genovese](https://www.cmu.edu/dietrich/statistics-datascience/people/faculty/chris-genovese.html)
  {: .course-item #course36218 }

  A class with a bad enough reputation among CS students that its reputation even spread to advisors. For context, there are two introductory probability course options that are one semester long for CS students: this and Probability and Computing (15-259). The latter is much more rigorous than the former and is often agreed upon to be a better-taught/structured course. So, how did I end up taking 36-218? 15-259 conflicted with 15-213 and I wanted to get my probability requirement done ASAP to take theoretical machine learning courses. I am pretty convinced that the conflict was intentional. These things aside, my main peeves from the class are its pacing and methodology. Trust me on this, the class _really, really, really_ took its time moving between topics. 80-minute lectures generally had 15 minutes of actual content with the remaining time taken by repetitive examples. I understand the idea of the class was to provide an easier one-semester probability course option that gave students an intuitive understanding of related concepts. However, the end result was just a course that left students with a shallow understanding of probability. Moreover, in an attempt to provide students with better intuition, the instructor tried a more hands-on-focused approach by developing a library specifically for the class to do things like sampling. I really disliked this approach since it turned a class that was supposed to teach foundations of probability into a class teaching how to use a mystical new library, which meant students missed out on key knowledge necessary in machine learning fields. This all said, I will give some leniency towards the course granted that it did come into existence somewhat recently. Still, I very much hope that it becomes better developed since right now, the only goal successfully checked off is a much easier experience than 15-259.

- 16-385 [**Computer Vision**](https://16385.courses.cs.cmu.edu/fall2024/), [David Held](https://davheld.github.io/)
  {: .course-item #course16385 }

  I had originally taken this class since I couldn't get into Natural Language Processing (11-711), but it ended up being a very nice experience. This is a project-based class, meaning there is the incredibly awesome benefit of not having to deal with any quizzes or exams. Instead, each lab is composed of a small written theory portion paired with a larger related programming component. The first half of the course is focused on more classical aspects of computer vision such as Hough transforms and homographies. The remaining half focuses on more modern techniques (mostly machine learning methods). Do note that some of the more advanced topics like GANs, VAEs, and diffusion models near the end of the course can end up being overwhelming based on your background (students' backgrounds for this class are very varied given its lax prerequisites). However, while lectures cover a tremendous amount of theory (which may come off as intimidating for the first few weeks), the actual assignments require only knowledge of a fraction of the lecture content. Still, the topics are very useful to know, especially if you plan to dive deeper into computer vision. Overall, I would strongly recommend this class if you want a generally stress-free but comprehensive introduction to computer vision.

- 85-211 **Cognitive Psychology**, [Zsuzsanna Kocsis](https://www.cmu.edu/ni/people/faculty/zkocsis.html) and [Emilia Ezrina](https://www.cmu.edu/dietrich/psychology/directory/core-training-faculty/emilia-ezrina.html)
  {: .course-item #course85211 }

  I took this to satisfy my category one humanity Gen-Ed requirement, mainly since it counts for both CS + AI major requirements. The course structure was fairly lax, consisting of open-internet exams/quizzes and two short-response homework assignments. While I don't think any of the course content is directly applicable towards honestly any part of my academic goals, I will say that understanding topics such as how the brain functions and the importance of sleep (particularly why) has been helpful. Once in a while, the course also covers some interesting or entertaining experiments such as the [the Wug Test](https://gsas.harvard.edu/news/all-you-need-wug) which is quite nice. If someone happens to need a Gen-Ed requirement from this category, I would definitely direct them to this class. Do keep in mind though that from what I heard, the structure of the course greatly varies between instructors, and that it has been supposedly very time-consuming in iterations taught by other professors.

- 15-210 [**Parallel and Sequential Data Structures and Algorithms**](https://www.cs.cmu.edu/~15210/), [Guy Blelloch](https://www.cs.cmu.edu/~guyb/) and [Charlie Garrod](https://www.cs.cmu.edu/~charlie/)
  {: .course-item #course15210 }

  More functional programming yay! I would call this class the first algorithms course CS majors take and it is done entirely with Standard ML. The course covers core parts of functional programming algorithm design like scan, fold, and iterate as well as more traditional concepts including dynamic programming and graph algorithms. Most iterations of the course have some sort of homework/quiz bucket system; attendance for recitation and lectures is also bucketed. I liked this course a lot most definitely because of its functional aspect; there is something about how this constraint forces you to think elegantly when identifying what subproblems are present and how to solve them recursively. Some advice for this course is to show up to recitations--the examples TAs go over end up being very helpful for the homework--and read the lecture notes (which I honestly found to be better than the lecture). My one qualm for the class is that it is somewhat lacking in transparency with how grades are calculated. Still, it was a relatively fun experience.

  Overall, my personal opinion is that this class is nice to take as early as possible since it teaches you the algorithmic skills required in technical interviews; many of the coding questions I get asked end up a lot easier than the homework problems from this class.

Units: 54

<a name="Systems-Disinterest">
This was a somewhat uneventful semester for me. I didn't find any of the courses extraordinarily interesting or enlightening, though most of them ended up being fun for some reason or another. Still, that doesn't mean I would choose different courses for this semester if I had a do-over. To be honest, however, taking the intro to computer systems course has somewhat led me to realize my disinterest in most computer system-related domains. I don't particularly enjoy working on low-level concepts like file systems or memory management and find them frustrating to debug. 
</a>

I do feel unsatisfied with the probability class I had chosen this semester, and I feel a bit lacking in that area, so I plan to take a graduate-level probability course to polish up eventually, likely in my junior year. If you end up having the option between 36-218 and 15-259 as a probability requirement, I would _really_ recommend the latter.

A habit I did end up picking this semester that I felt made my days more productive is sleeping and waking up early. I would really recommend this since, at least to me, it's a lot easier to get things done in the morning since there are fewer distractions. I've also found that the usual morning headaches I get after waking up to an alarm disappear if I wake up naturally; that's only possible when I sleep early enough lest I end up late to class.

### Summer 2025 (Remote)

{: .first-course-item #course82279 }

- 82-279 **Anime - Visual Interplay between Japan and the World**, [Yoshihiro Yasuhara](https://www.cmu.edu/dietrich/lcal/about-us/filter/faculty/yoshihiro-yasuhara.html)

  This satisfied my category three humanity Gen-Ed requirement! From the name, you can assume this class was gonna be relatively tame. The structure of the class was essentially to watch a few episodes of an anime or movie, do a reading, and write reflections about each of them. The class covered a range of influential shows ranging from older works like Astro Boy to more recent trends like Attack on Titan. Essentially everything included was a good watch (except for Paprika... I CANNOT deal with psychological/horror films) and the responses were generally graded pretty leniently so the course was a fantastic take. I did, however, take this during the summer since there was the option of doing it remotely so the experience in person may be different. That said, I can't imagine this course becoming something not relaxing. The one thing is that this course did not feel particularly rewarding for me to do.

Units: 9

### Spring 2024

{: .first-course-item #course21266 }

- 21-266 **Vector Calculus for Computer Scientists**, [Clive Newstead](https://www.math.cmu.edu/~cnewstea/)

  A multivariable calculus course for CS majors is required as a prerequisite for probability courses. I don't really have much to comment about this class--I think it was a good balance between theory and computation. If I had to mention anything, it'd be that the second half of the course felt a bit rushed in terms of timing and that sometimes the scratchwork for homework would be unusually tedious. The exams felt appropriate in that the material covered was simply an extension of homework concepts and was typically pretty similar to the practice tests--the only thing was it was a bit of a time crunch if you don't immediately see what direction you should take for a question. Notes were similar to 21-241 in that a template was always provided. I will note that the final was much harder than the midterms; keep that in mind while taking the class. This was in general just a solid class without much to comment about.

- 15-251 **Great Ideas in Theoretical Computer Science**, [Anil Ada](https://www.pandanotes.org/servers/anil/)
  {: .course-item #course15251 }

  An introductory class about theoretical computer science concepts. Originally, I had decided to take this class so that I could take PnC (15-259) next semester (this did not happen since it would conflict with another core class 15-213). While I believe the class was mostly well taught, I did not enjoy the structure very much. The pace of the latter half of the course felt a bit rushed in which various topics would be only covered at a higher level/quite briefly. This meant that problems tended to have hand-wavy solutions, though I suppose the entire course felt pretty hand-wavy. Personally, I would've enjoyed more depth into the topics of the latter half of the class by either cutting down on the topics covered or speeding up the first half of the course. That said, I do think the contents of the class, especially complexity theory, were very interesting. One of my biggest regrets for the class was actually signing up for mandatory attendance since 1. I am SUPER not a morning person and 2. The points from mandatory attendance did not do anything to my grade (in fact probably lowered it) since it only counts towards homework. I'll mention that homework is scored on an 80% or so bucket system so it's not difficult to earn a full score and that lectures are recorded so keep this in mind when deciding your attendance policy. The mentor system is so nice for this class too so make use of it. Anyway, I would advise only taking 15-251 if you plan on taking 15-259 over 15-213 the following semester (unless they decide to stop having these lecture times overlap).

- 15-150 **Functional Programming**, [Michael Erdmann](https://www.cs.cmu.edu/~me/whois-me.html)
  {: .course-item #course15150 }

  The greatest class EVER. That I have finished so far. The class starts off a bit slow with the basics of functional programming and recursion but ramps up to more exciting topics like higher-order functions and continuation-passing style. The exams were honestly a bit underwhelming for the class and to be blunt... too easy. That aside, the programming homework was fun and felt like solving a puzzle--not too easy as to be unrewarding but not so hard as to be frustrating. The class has definitely done a good job in increasing my understanding of parallel algorithms and in general, how to break coding problems into parts. The only reason the class is not a 10 for me is that I wish it had more theory components into it... the class is pretty hands-on with not as many analytic components.

- 84-275 **Comparative Politics**, [Ignacio Arana Araya](https://ignacioarana.org/)
  {: .course-item #course84275 }

  This was just a class to satisfy category two of my general education humanities requirement. Was the class easy? Yes. Did I learn anything? Not really. This course had no homework so it was a relatively low time commitment... I just needed to do a somewhat short reading before every class in preparation for the quiz. The midterms and final were also easy considering that the potential questions are given two weeks before the exam and you just have to prepare responses. So, yeah... the 6/10 in my rating is completely due to the relaxed nature of the class.

- 76-106/76-107 **Writing about Literature/Writing about Data**, [Chap Morack](https://www.cmu.edu/dietrich/english/about-us/phds/bios/chap-morack.html)/[Ben Markey](https://www.cmu.edu/dietrich/english/about-us/phds/bios/ben-markey.html)
  {: .course-item #course76106-76107 }

  More classes I don't really have much to say about. The classes were both basically entirely participation-based so as long as you did the work, you'd pretty much be guaranteed an A. I guess I was able to read some interesting short stories/research from these classes but the classes as a whole were both boring and felt a bit useless.

Units: 52

My experience with classes this semester compared to my last semester was such a contrast that I'm convinced they intentionally made the first semester bad to beat people into shape. Anyway, I was quite satisfied with the courses I took (except for the English classes) and would recommend taking the rest of them. I started my assignments earlier this semester which definitely helped relieve stress and made better use of my available resources (Piazza and TAs). The only thing I would've done differently, however, is to take 15-213 first instead of 15-251 since 15-213 was the requirement for more classes and probably looks much better on a resume haha... Also, I probably should've started applying for internships sooner this semester whoops-

### Fall 2023

{: .first-course-item #course03151 }

- 03-151 **Honors Modern Biology**, [Jonathon Minden](https://www.cmu.edu/bio/people/faculty/minden.html)

  This was an advanced introductory course in modern biology for students who had prior AP Biology credit. I'll be honest, I don't know why I took this course originally apart from the thought that biology was pretty cool--that said, it was a nice change of pace relative to my other classes. Aside from the first unit on chemistry, the content covered was entirely new, building off from an assumption of basic prior knowledge. The class was fast-paced and covered a wide amount of topics, ranging from a deeper dive into DNA synthesis to understanding the GTPase cycles. For the most part, practice exams and lectures were more than sufficient in preparation for the exams, though the large amount of content was always daunting. The course tended to be exclusively lecture-focused, meaning it was difficult to fill gaps in knowledge whenever I had to miss class. One thing I will complain about is that this class hosts its office hours at the Mellon Institute, a 20-minute walk which was incredibly aggravating. Another note is this class has like... 5 exams and a final? There was an exam drop though. Overall, I had a mostly good time with the class and made friends with quite a few people outside my department.

- 21-241 **Matrices and Linear Transformations**, [David Offner](https://www.cmu.edu/math/people/faculty/offner.html)
  {: .course-item #course21241 }

  As much as I joked with friends about the class being too hand-wavy, it was one of the classes during my first semester that I liked more. The lectures felt very structured and came with an outline of the important points--moreover, there was a surplus of supplemental materials and practice tests. While a bit lenient on proofs, the fast-paced tests did engrave in me many key ideas of linear algebra I see in my other classes e.g. Computer Vision. One point I would like to add though is to this day, I still do not understand why there is a final project in Julia. It seems... very pointless to say the least, especially given that recitations existed essentially only to teach it? Please let us use Python for the love of my favorite stuffies ;-;. But yeah, this class was very solid and a chill one to take. My salutations to David Offner teaching this class his last semester.

- 15-122 [**Principles of Imperative Computation**](https://www.cs.cmu.edu/~15122/)
  {: .course-item #course15122 }, [Iliano Cervesato](https://csd.cmu.edu/people/faculty/iliano-cervesato)

  Essentially our introductory data structures course. I will admit, the first exam was incredibly rough but the class difficulty curved significantly down after that. Extra credit from assignments was helpful and the tests became less demanding. I'd like to think the most fun part about the course is the programming assignments which are very hands-on but reasonable. Except for the Huffman assignment. That was pure evil. I will note that the class did not cover as many details of algorithms as I would have liked. Also, I think it is infinitely more annoying now than before given there are weekly "writing sessions" _and_ proctored quizzes. Still, as much as this class is hated, credit needs to be given where it's due for being thorough in its content.

- 15-151 [**Mathematical Foundations for Computer Science**](https://www.math.cmu.edu/~jmackey/151_128/welcome.html), [John Mackey](https://www.cmu.edu/math/people/faculty/mackey.html)
  {: .course-item #course15151 }

  This was our introductory discrete math class. I might have come into CMU with a negative math background so this was a bit of a struggle. That said, the class did a pretty good job bringing me back to pace but it was easily my most time-consuming class this semester--I would spend infinite time on every other homework assignment in the first half of the course. This is partly because the class was held to an unreasonable amount of rigor on the small details in the beginning. I think the course did get easier after that breakpoint in becoming more lenient. Still, I despise (at a personal level) this class for just giving me a tough time... I will, however, admit this class was well-taught.

- 07-131 **Great Practical Ideas in Computer Science**
  {: .course-item #course07131 }

  I guess this was kind of useful? I don't have much to say about this since I stopped attending the weekly lectures after the first couple weeks since I realized there was nearly nothing I didn't know prior--this class just gave me some extra weekly chores. I suppose it would be a bit useful for people who have no experience with Git, the terminal, and things similar. The highlight of this class was the Pokemon lab and an unnamed individual's accidental deletion of pidgey.txt.

- 07-128 **First Year Immigration Course**
  {: .course-item #course07128 }

  Random time-sink class? There were some interesting topics covered but for the most part, I just found mandatory attendance for this annoying. This was especially because of how the class was near evening and I would have gone through 4 or so classes already... too tired to sit through another hour of content I was usually not interested in. I'm almost certain so many others shared the same thought given how much Veronica Peet egged on people for not showing up haha.

Units: 50

My first semester was honestly the worst out of all mine so far (at this time that would be up to the third semester). So, for those having a difficult first semester... it gets better I promise!!! It was a bit difficult to adjust to college life and getting cooked by 15-151 did not help. My eating schedule had become terrible, not to mention the rest of my health. Having friends to go to probably was a huge reason I got through it so I really appreciate them. I cannot emphasize how important it is to try talking to new people. This ties to what I regret most, which is not reaching out to more people in the first semester since it gets harder later on. My biggest takeaways from this semester were just to start homework early and make use of office hours (before the deadline or the line gets UNBEARABLE).

---

## CMU Courses FAQs

This section is a modification of Fan Pu's CMU-Specific FAQ found [here](https://fanpu.io/courses/) and aims to provide insight for people unfamiliar with CMU course conventions and/or policies.

### Course Numbers

From [a note regarding course numbers](http://coursecatalog.web.cmu.edu/previous/2017-2018/schoolofcomputerscience/courses/):

> Each Carnegie Mellon course number begins with a two-digit prefix which
> designates the department offering the course (76-xxx courses are offered by the
> Department of English, etc.). Although each department maintains its own course
> numbering practices, typically the first digit after the prefix indicates the
> class level: xx-1xx courses are freshmen-level, xx-2xx courses are sophomore
> level, etc. xx-6xx courses may be either undergraduate senior-level or
> graduate-level, depending on the department. xx-7xx courses and higher are
> graduate-level. Please consult the Schedule of Classes each semester for course
> offerings and for any necessary prerequisites or corequisites.

Some of the more common ones you might see as a CS major include:

- 15-xxx: Computer Science
- 21-xxx: Mathematical Sciences
- 02-xxx: Computational Biology
- 05-xxx: Human-Computer Interaction
- 10-xxx: Machine Learning
- 11-xxx: Language Technologies Institute
- 16-xxx: Robotics
- 17-xxx: Institute for Software Research
- 18-xxx: Electrical & Computer Engineering
- 98-xxx: Student Led Courses

### Unit System

Many universities use a semester credit system such that one credit corresponds to three hours of work. CMU differs in that regard by using a unit system that represents the expected number of work hours for an average student. So, three units are the same as one traditional semester credit. Note that lecture time is included in the context of work hours.

### Overload Policy

In the _School of Computer Science_, students have a unit cap of 54. Unit overload requests must be submitted to your academic advisor, contingent on past academic performance.

First-year students are not permitted to overload.

### What are StuCos?

_Student Taught Courses_ (StuCos) are low-stress classes taught by fellow students and can be on any topic not available through regular university offerings. Previous topics include improv comedy, type theory, tea culture, and many others. StuCos are pass/fail courses and three units each. Note that these units do not count towards the overload limit.

### Special Topics Courses

The Computer Science Department offers Special Topics in Theory courses, numbered 15-859. The section numbers differentiate the specific course. For instance, 15-859 CC is Algorithms for Big Data.

These are irregularly offered courses targeted at people intending to pursue research in the field.
