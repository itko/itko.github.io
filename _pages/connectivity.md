---
title:  Connectivity
permalink: projects/connectivity/
layout: project
author_profile: false
---
# Connectivity

*How do we get from a satellite image to a weighted network? The following is a summary of the work I did at the Ecosystem Management Group at ETH Zurich. The full publication can be [found here](https://drive.google.com/file/d/0B153rgUR-lZ9ZWptMG9YQTB1LU1YOWFVRGI0RGhsVVBjT2h3/view?usp=sharing).*

<div class='side-by-side'>
<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/borneo_zoom.svg"
	    src="/assets/images/projects/connectivity/borneo_zoom.svg">
	    <img
	    data-src="/assets/images/projects/connectivity/graph_circular.svg"
	    src="/assets/images/projects/connectivity/graph_circular.svg">
</figure>
</div>


## Motivation
When it comes to deforestation, it's better to lose a smaller area of forest than a larger one. While true, that's not the whole story. The more forests we cut down, the patchier the remaining forest becomes, and the harder it is for animals to move between these patches.

Therefore, when measuring the impact of deforestation, we need to move beyond a simple measure of the area of forest that is cut. We need to start measuring the *connectivity* of forests.

## Recipe
So how do we measure the connectivity of a network of forest patches? Let's start with a satellite image of our area of interest. In this case, let's examine a region next to Kota Kinabalu, in Borneo:


<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/borneo_zoom.svg"
	    src="/assets/images/projects/connectivity/borneo_zoom.svg">
</figure>

This is just a flattened satellite image, in reality there's hills and mountains. So let's combine the above satellite image with another satellite image, this time for elevation:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/with_elevation.svg"
	    src="/assets/images/projects/connectivity/with_elevation.svg">
</figure>

From space, the whole area looks like it's forested, but in reality there's actually quite a bit of open spaces. Let's classify our region based on these land-use types:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/with_elevation_and_regions.svg"
	    src="/assets/images/projects/connectivity/with_elevation_and_regions.svg">
</figure>

Now that our satellite image is ready, we can look at how it affects the movement of animals. For example, let's focus on Everett's White-eye, a bird native to the area. Here is its range, as one would draw it on a texbook:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/with_elevation_and_regions_and_range.svg"
	    src="/assets/images/projects/connectivity/with_elevation_and_regions_and_range.svg">
</figure>

But this is just the nominal range. In reality, Everett's white eye's stays away from open areas and from high elevations. When we filter the image for these preferences, the range is actually much patchier:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/habitat_with_elevation.svg"
	    src="/assets/images/projects/connectivity/habitat_with_elevation.svg">
</figure>

So now we have a bunch of forest patches representing the habitat of our species. How can we represent it as a network? For clarity, let's start by plotting the centroid of each patch. These represent the nodes of our graph: 

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/habitat_with_centroid.svg"
	    src="/assets/images/projects/connectivity/habitat_with_centroid.svg">
</figure>

In order to connect the nodes, we need to understand how our species move from place to place. For this, we incorporate a model of species movement between forest patches, which is based on several parameters, such as the distance and vegetation between forest patches, the weight of the species, etc.

Using this model we can estimate the probability that different species will travel from one forest patch to another. Here it is for Everett's White-eye (thicker is higher probability):

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/habitat_with_centroid_and_probs.svg"
	    src="/assets/images/projects/connectivity/habitat_with_centroid_and_probs.svg">
</figure>

To really drive home the point, we can transform the graph into a circle:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/graph_circular.svg"
	    src="/assets/images/projects/connectivity/graph_circular.svg">
</figure>

And there we have it: our final graph. We can see that some paths are more probable than others, and we can already see that some patches are "busier" than others. 

With this we can start asking interesting questions, such as "Which forest patches are most important to protect?", or "Where should we regrow forests in order to improve connectivity?"

## Conclusion
To maintain biodiversity, animals need to be able to move around. By thinking of forests as nodes of a graph, we can start to understand how and where to focus our conservation efforts.