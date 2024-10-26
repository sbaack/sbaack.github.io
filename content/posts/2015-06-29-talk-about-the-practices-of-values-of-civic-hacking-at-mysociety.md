---
title: Talk about the practices of values of civic hacking at mySociety
date: 2015-06-29
tags:
- conferences
- civic tech
---

Last week I gave a talk at the great [Data Power Conference](https://web.archive.org/web/20151216174345/http://www.sheffield.ac.uk/socstudies/datapower/programme) at the University of Sheffield which had a [panel dedicated to civic hacking](https://web.archive.org/web/20160822003422/http://www.sheffield.ac.uk/socstudies/datapower/panel-9). This was a great opportunity to present some findings from my ongoing case study about the practices and values of civic hacking at mySociety.

The slides can be found [here](https://web.archive.org/web/20160909113343/http://www.slideshare.net/sbaack/data-power-and-civic-hacking-at-mysociety).

### Empowerment and civic hacking

My presentation revolved around the term *empowerment*. mySociety aims at empowering citizens, but what does 'empowerment' actually mean in relation to civic hacking? Based on a content analysis (which included mySociety websites, project descriptions, blogposts) and a couple of interviews, my answer to this question is currently twofold:

1. *Civic hacking aims at giving citizens a greater sense of agency by making it easier for them to engage with authority*

[FixMyStreet](https://web.archive.org/web/20150627191717/https://www.fixmystreet.com/), mySociety's website for reporting local issues to local councils, is a nice example to illustrate this point. At first, it might not be very obvious what reporting potholes, broken street lights, or [dog poop](https://web.archive.org/web/20150719185248/https://www.mysociety.org/2015/04/24/new-poster-to-help-with-dog-fouling-in-your-area/) has to do with empowerment. However, mySociety didn’t build FixMyStreet because they were particularly concerned with how smooth or clean the streets in their neighborhoods are. It rather has to do with "adjusting power relationships"[^1]:

> If somebody is able to report a problem with a pothole outside their house and next week it's fixed, **they have learned that engagement with authority is not futile**...FixMyStreet is a gateway drug into bigger civic engagement.

To further understand this statement, it helps to look at some of reasons why mySociety decided to build FixMyStreet back in 2007. The basic problem they wanted to address was that reporting local issues was often not an easy and straightforward process for citizens. First, citizens often didn't know who is responsible for fixing an issue because each area in the UK has two councils with different responsibilities. Second, mySociety found that the websites provided by the local councils were not user friendly. These websites were designed to best serve the administrative processes of the councils and usually required the user to fill out a rather technical form (which often was not easy to find). With FixMyStreet, mySociety aimed at making this process as intuitive and easy as possible for citizens. As a user of the site, you basically just have to click on a map to locate the issue, give a description of the issue and send the report. Based on where you’ve clicked on the map and what type of issue you’ve reported, FixMyStreet will then forward your report to the local council that is responsible for fixing it.

In short, mySociety tried to turn reporting local issues from something that requires some time, research and energy into something that people can do *along the way* -- and I suggest that this is essential for the meaning of empowerment in relation to civic hacking. It means to give citizens a greater "**sense of agency**" by developing tools that make it easier for them to engage with authority in a successful way. One consequence of this is an emphasis on a good user experience for the "citizen user", i.e. on making processes easier from the perspective of the citizen even if that means making it less convenient for government institutions.

2. *Civic hacking aims at empowering citizens by making government activities more legible to them*

I suggest that the second dimension of empowerment in civic hacking is about creating a new level of legibility for citizens, which often requires access to certain types of structured data. This is where seemingly purely technical details about data structures, open standards, and formats play a major role.

A good example to illustrate this is [TheyWorkForYou](https://web.archive.org/web/20150630143439/http://www.theyworkforyou.com/). This website is only possible because mySociety was able to scrape the information available on the official parliament websites in the UK in order to turn this information into structured data. 'Structuring data' means to identify specific pieces of information in a larger data set in order to mark these pieces of information with an identifier. These identifiers can then be used to filter and analyze the data in new ways. For example, to be able to filter out speakers in parliamentary discussions, each speaker has to be marked as a speaker with an identifier. By turning information about the activities of the parliaments into structured data, mySociety is thus able to filter and organize this information in new ways. I just want to point out one aspect to illustrate my argument: the possibility to combine searches for certain keywords with email alerts. Users of TheyWorkForYou can for example search for 'climate change' and then sign up to get an email every time someone in parliament is using this keyword in a speech. This can make it easier to keep track of how certain issues are discussed in parliament, i.e. how different members of parliament from different parties talk about climate change.

How does this create a new 'level of legibility'? To understand this, it is important to note that parliaments in the UK already publish transcripts of speeches online, but usually as PDF files. It is possible to download and search in these PDFs, but it would then require much more time and energy to filter out specific pieces of information. Moreover, to keep track of how certain issues are discussed in parliament, it would be necessary to repeat this process regularly. Similarly to what I described in relation to FixMyStreet above, mySociety aimed at turning this process into something people can do along the way, without investing a lot of time and energy — users just need to sign up for the alerts once and then get an email from time to time. With 'creating a new level of legibility' I mean that empowerment in civic hacking is not just about transparency -- the parliaments already made transcripts of speeches available online -- but also about **enabling** citizens to keep track of what their government is doing in a very practical sense. In other words, it is not only about giving citizens the theoretical means of keeping track of their government by 'somehow' making information available, but also about giving them a greater capacity of doing so by making this information more accessible and actionable for them.

### Ongoing research

Please note that these are *early* findings on a specific aspect of my study. However, I'm excited about how rich, insightful and interesting these early steps are already and I hope to be able to do more interviews with members of mySociety in the near future!

[^1]: All quotes used in this article are taken from my interviews with members of mySociety.