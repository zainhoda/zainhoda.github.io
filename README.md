---
layout: page
title:  "Links"
permalink: /
---

# What I'm Working On
- [Bazog](https://bazog.com/): an AI-enabled app that lets you create short video slideshows from text And images
- [Hownova](https://apps.apple.com/us/app/hownova/id1630216185): How-to videos you can actually use. Video for each step loops until you're ready to move to the next step. Available as an [App Clip](https://app.hownova.com/share/WkfplFDORE63tiTTahEr).

# My Favorite Programming Languages
[Swift](https://www.swift.org/), [Elm](https://elm-lang.org/), [Go](https://go.dev/), [V](https://vlang.io/)

# My Previous Side Projects
Most of these projects are incomplete and I might pick up some of them again later as need or inspiration arises.
- [swiftui.gallery](https://swiftui.gallery/): A gallery of SwiftUI code example snippets and their resulting views. This was useful when SwiftUI was first released. Now, I'd recommend the [DetailsPro](https://detailspro.app/) app instead.
- [Wordwall](https://zainhoda.github.io/wordwall/): Simple Elm app that uses the browser's built-in text-to-speech API to enable kids to learn to spell words.
- [GraphQL UI](https://github.com/zainhoda/graphql-ui): Point to any GraphQL backend to automatically generate an admin interface using GraphQL's introspection and metadata. Super complicated data structures don't work but basic and medium complexity structures work fine. Think of this as something like Retool without an intermediate backend -- it's just a JS file that you include.
- [Orbgo](https://github.com/zainhoda/orbgo): Beginnings of Tableau-like interface that allows you to drag and drop fields from a data frame and create visualiztions. It does this using Python Pandas and shows you the generated Pandas code.
- [MBS Pricer](https://github.com/zainhoda/mbs-pricer/blob/main/Write%20Up/mbswriteup.pdf): A C++ Excel plugin that lets you put in assumptions and generate price estimations for mortgage-backed securities.
- [Spinning Wheel](https://zainhoda.github.io/spinning-wheel/): A toy Elm app that I wrote to learn the basics of Elm. 
- [Vizit](https://medium.com/@zain_hoda/vizit-what-a-mobile-app-looked-like-before-the-iphone-d436f781795d): A location-based mobile app for the Palm-treo. This pre-dates iPhone apps by several years. For positioning, it had a separate GPS attachment that plugged into a slot at the top of the phone.

# Posts
<ul>
  {% for post in site.posts %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }} <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
