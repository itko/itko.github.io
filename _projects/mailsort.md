---
title: "mailsort"
header:
  teaser: /assets/images/projects/mailsort.png
excerpt: "Using machine learning to sort through email"
---

Machine learning is one of those few things that when you start reading about it
you start seeing its applications everywhere. I was keen to hop on the bandwagon
and finally start implementing it in a project.

## Problem
It's quite simple: as it stands, the gmail filtering options are not very comprehensive.
For example, there is no option to filter according to dates. But more important
than the lack of options is the fact that the filters require the the user to be familiar
with the emails he wants to sort: he would need to know who sent them, what subjects
they contain, etc.

<figure>
	<img src="/assets/images/projects/mailsort-filter.png" alt="filter example" width="200">
	<figcaption>Options available when creating a gmail filter</figcaption>
</figure> 

What this means is that while my filters are able to correctly label many
the emails I want to sort, due to my filters not being comprehensive enough about 30%
of emails which should be labeled end up unlabeled. This leaves me with a bunch of
partially sorted emails, which is more annoying than not sorting them at all!

## Solution
We need to find the current pattern in the email labels and use this
pattern to sort the unlabeled emails. For this, we employ machine learning.

### Machine Learning
I know what you are going to say: why jump immediately to machine learning when it might be possible
to accomplish the task in a simpler way? You're right, I should
look into other approaches. But this is so much more fun!

That being said, this problem screams machine learning. Specifically, this is a multi-label classificationproblem. I have a set of labeled data which is composed of a large amount of samples (5000 emails, not huge but definitely workable). Each email can be labeled, and, importantly, it can have multiple labels at the same time (Youtube videos sent by my brother can be filed under both 'Family' and 'Videos').

### Implementation
1) Raw data collection. This includes the emails, the threads they belong to, their headers (date, from, to, subject), etc. This can all be retrieved using the gmail API.

2) Preprocessing and feature extraction. Much of this follows standard text classification procedures (assigning freqeuncy to words, encoding labels, etc.)

3) Selecting and training a classifier.

4) Testing, testing, testing.

5) Assign email labels according to the model prediction (using the gmail API).

6) Bonus: convert to an on-line system, where the model is retrained in real-time based on new emails.
