---
title: ""
summary: ""
date: 2026-06-08
type: landing

sections:
  - block: resume-biography-3
    id: about
    content:
      username: me
      text: ""
      headings:
        about: Summary
        education: Education
        interests: Interests
  - block: legacy-experience
    id: experience
    content:
      title: Experience
      username: me
    design:
      date_format: "Jan 2006"
  - block: legacy-awards
    id: accomplishments
    content:
      title: Accomplishments
      username: me
    design:
      date_format: "Jan 2006"
  - block: legacy-collection
    id: posts
    content:
      title: Recent Posts
      cta:
        text: See All Posts & Media
        url: https://halfrost.com/
      filters:
        folders:
          - post
        exclude_featured: false
      count: 5
      order: desc
  - block: legacy-portfolio
    id: projects
    content:
      title: Projects
      cta:
        text: See All Projects
        url: https://github.com/halfrost
      filters:
        folders:
          - project
      buttons:
        - name: All
          tag: "*"
        - name: Deep Learning
          tag: Deep Learning
        - name: Algorithm
          tag: Algorithm
        - name: Mobile
          tag: Mobile
        - name: Other
          tag: Other
  - block: legacy-collection
    id: publications
    content:
      title: Recent Publications
      cta:
        text: See All Publications
        url: http://books.halfrost.com/
      filters:
        folders:
          - publication
      count: 5
      order: desc
  - block: legacy-collection
    id: talks
    content:
      title: My Recent Talks
      cta:
        text: See All Talks
        url: https://speakerdeck.com/halfrost/
      filters:
        folders:
          - talk
      count: 5
      order: desc
  - block: legacy-skills
    id: skills
    content:
      title: Skills
      username: me
  - block: legacy-contact
    id: contact
    content:
      title: Contact
      email: i@halfrost.com
      address: Changqiao, Xuhui, Shanghai 200000, China
      social:
        - label: DM Me
          icon: brands/twitter
          url: https://twitter.com/halffrost
---
