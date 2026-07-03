---
title: Getting acquainted with the JupyterHub and Jupyter Book communities
authors:
  - name: Serena Bonaretti
    github: sbonaretti
    url: https://sbonaretti.github.io/
date: 2026-06-30
license: CC-BY-4.0
---

In this first month as a JupyterHub and Jupyter Book community manager, I introduced myself and spent quite some time getting to know people and the projects they work on. 
I also started to expand my technical competences and contribute to the Collaboration Cafes, and I participated at a Jupyter Community Workshop. 


## Introducing myself to the broader Jupyter Community
One of the first  things I did was to write a post for the Jupyter Blog [introducing myself and my new role]( https://medium.com/jupyter-blog/becoming-the-new-jupyterhub-and-jupyter-book-community-manager-481d864947d4). As I mentioned there, I am very excited to take on this role and work with all the people involved in JupyterHub and Jupyter Book.


## Getting to know the people and the projects they work on
People are at the heart of JupyterHub and Jupyter Book, and getting to know them is a privilege. I had the opportunity to introduce myself to several maintainers and contributors and learn about their work, interests, and perspectives. From these conversations, I realized that I work with people who **deeply care** about what they do and are remarkably generous in sharing their knowledge and experiences.

Beyond the personal introductions, these conversations helped me learn the history of both JupyterHub and Jupyter Book, including their successes and challenges. For JupyterHub, I also became familiar with the recent [Voices of JupyterHub](https://voicesofjupyterhub.orgmycology.com/) report, the [User Workshop](https://jupytercon2025.sched.com/event/28H31/tutorial-jupyterhub-user-workshop-arielle-bennett-the-alan-turing-institute-beth-duckles-dan-sholler-organizational-mycology-min-rk-uc-berkeley-additional-fee-pre-registration-required?iframe=no&w=100%&sidebar=yes&bg=no) at JupyterCon 2025 and the [Roadmapping Workshop](https://events.linuxfoundation.org/roadmap-workshop-for-jupyterhub-and-binder/) held last February, all aimed at determining the focus of the project for the coming years. For Jupyter Book, I learned about its [evolution](https://proceedings.scipy.org/articles/hwcj9957) from the [Sphinx](https://www.sphinx-doc.org/en/master/)-based version 1 to the [MyST](https://mystmd.org/)-based version 2, and the challenges that accompany such a transition phase. For both projects, I was also introduced to their GitHub organizations with their many repositories and documentation websites, which I am continuing to explore. 


## Expanding my technical competences
Although my role is not primarily technical (I am not expected to add new features or fix bugs), I believe that the better I understand the technical aspects of the projects, the more effectively I can support maintainers, contributors, and users. For this reason, I am continuously expanding my technical knowledge. 

I regularly participate in the weekly [MyST Working Sessions](https://jupyterbook.org/events/#working-sessions). During these meetings, I learn what the maintainers are currently working on (e.g., tools for API references or the creation of a new theme), and I have the possibility to ask clarifications about project designs and discuss potential new actions. 

I have also been improving my knowledge of **GitHub and Git**. Although I had used these tools for personal projects before, contributing to a collaborative open-source project is quite different. For example, I have to be more clear and precise when opening issues or sending pull requests, so that the maintainers can quickly understand and review my contributions. In addition, I am discovering GitHub features that I had never used before, such as [Projects](https://github.com/orgs/jupyter-book/projects), which provide a visual way to categorize and track issues and pull requests.  

One thing that I didn't expect to learn is that developers have their own **jargon**! The way I discovered this was quite funny. At the end of one meeting, two maintainers were listing some _outstanding_ tasks. To me, those tasks didn't sound _exceptional_ at all! So, I asked ChatGPT _What does outstanding mean for software engineers?_ and there it was: _To do_. At that point, I realized that I had also some translation work to do! So now I know that _to bump_ means _to update_, or _to ship_ means _to release_. My vocabulary expansion is just at the beginning!

I have also learned to use new **communication platforms**, such as [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub), used by the JupyterHub community, and [Discord](http://discord.mystmd.org/), used by the Jupyter Book/MyST community. I also became familiar with **open-source collaborative text editors**, that is, [HackMD](https://hackmd.io), which we use during technical meetings, and [Framapad](https://framapad.org/abc/en/), which we use to take notes during the Collaboration Cafes.


## Co-organizing the Collaboration Cafes
The [Collaboration Cafes]( https://compass.hub.jupyter.org/meetings/collab-cafe/) are biweekly meetings held on the first and third Tuesdays of each month, where maintainers, contributors, and users of JupyterHub and Jupyter Book come together to discuss ongoing work and community topics. So far, my work has mainly focused on archiving the notes in the blog of the [JupyterHub compass](https://compass.hub.jupyter.org/meetings/collab-cafe/2026/) via pull requests (e.g., Pull request (PR) [jupyterhub/team-compass/#917](https://github.com/jupyterhub/team-compass/pull/917)), opening a pre-meeting issue to collect the topics participants want to discuss at the following meeting (e.g., issue [jupyterhub/team-compass/#918](https://github.com/jupyterhub/team-compass/pull/917)), preparing the meeting note file, and sending reminders on the communication channels. In the coming weeks, I will also start hosting them!


## Participating in the MyST workshop

On June 15-17, I participated in the three-day Jupyter Community Workshop titled [Demystifying MyST in Education](https://events.linuxfoundation.org/demystifying-myst-markdown/), whose goal was to reduce barriers to adopting Jupyter Book and the MyST document engine for science educators. You can find a complete report that I co-authored with the organizer, [Chiara Marmo](https://cmarmo.codeberg.page/resume-html/), on the [Jupyter Blog on Medium](https://blog.jupyter.org/) in the coming days.

What struck me the most were the specific needs that **educators** have when creating **textbooks** with Jupyter Book! In their vision, notebooks are primarily a **collection of *text* cells** with only a few *code* cells - I have always thought of Jupyter notebooks in the opposite way, as I mainly use them for coding! As a consequence, educators would like *text* cells to support various writing languages (see the Jupyter Enhancement Proposal [enhancement-proposals/#138](https://github.com/jupyter/enhancement-proposals/pull/138)), just as _code_ cells can support various programming languages (Python, R, etc.). They would also like a centralized way to hide *code* cells and their outputs, so that student cannot see the solutions. 

Another interesting perspective was **student usability**. A Jupyter book should be easy to read and navigate on a mobile phone, as many students study while commuting. Having a high quality .pdf version is also important because many students like to take notes while studying (and this cannot be done on a website!) or have a printed version of the book to reduce screen time.

In addition to participating, I actively contributed to the workshop through several concrete activities, including updating the Jupyter Book documentation to enable deployment on GitLab Pages using pixi (PR [mystmd/#2959](https://github.com/jupyter-book/mystmd/pull/2959), later refined and replaced with improved GitLab deployment documentation, PR [mystmd/#2966](https://github.com/jupyter-book/mystmd/pull/2966)), clarifying the publishing tutorial by separating the main objective from alternative hosting options (PR [jupyter-book/#2635](https://github.com/jupyter-book/jupyter-book/pull/2635)), and capturing user feedback in a users’ wishlist (PR [jupyter-book/2636](https://github.com/jupyter-book/jupyter-book/issues/2636)).


_And that's it for this month! See you next month!_
