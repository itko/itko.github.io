---
title:  Connectivity
permalink: projects/connectivity/
layout: project
author_profile: false
---
# Connectivity

There's two images below, a satellite image and a weighted graph: 

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

How do we get from one to the other? The writeup below explains how we can use staellite imagery to model the movement of animals throughout a forest landscape.


## Intro
When it comes to deforestation, it's better to lose a smaller area of forest than a larger one. While true, that's not the whole story. The more forests we cut down, the patchier the remaining forest becomes, and the harder it is for animals to move between these patches.

In other words, the more well-connected a forest is, the more biodiversity it can sustain. Therefore, we need to account for connectivity when measuring deforestation.

## Recipe
So how do we measure the connectivity of a network of forest patches? Let's start with a satellite image of our area of interest. In this case, let's examine a region next to Kota Kinabalu, in Borneo:


<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/borneo_zoom.svg"
	    src="/assets/images/projects/connectivity/borneo_zoom.svg">
</figure>

This is just a flattened satellite image, in reality there's hills and mountains. It's important to account for this, because elevation affects the movement of species:

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

Now that our satellite image is ready, we can look at how it affects the movement of animals. For example, let's focus on Everett's white-eye, a bird native to the area. Here is its range, as one would draw it on a texbook:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/with_elevation_and_regions_and_range.svg"
	    src="/assets/images/projects/connectivity/with_elevation_and_regions_and_range.svg">
</figure>

But this is just the nominal range. In reality, Everett's white eye's stays away from open areas and from high elevations. Therefore, the actual range is actually much smaller (and patchier!):

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/habitat_with_elevation.svg"
	    src="/assets/images/projects/connectivity/habitat_with_elevation.svg">
</figure>

So now we have a bunch of forest patches representing the habitat of our species. Now we need to find a way to represent it as a network. For clarity, let's start by plotting the centroid of each patch. These represent the nodes of our graph: 

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/habitat_with_centroid.svg"
	    src="/assets/images/projects/connectivity/habitat_with_centroid.svg">
</figure>

In order to connect the nodes, we need to understand how our species move from place to place. For this, we turn to a formula which models the movement of species between forest patches as a factor of distance, the type of land between patches, as well as some other factors, such as the weight of the species.

Using this model we can generate some probabilities for a species travelling from one forest patch to another:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/habitat_with_centroid_and_probs.svg"
	    src="/assets/images/projects/connectivity/habitat_with_centroid_and_probs.svg">
</figure>

We can see that some paths are more probable than others, and we can already see that some patches are "busier" than others. To really drive home the point, we can plot the graph as a circle:

<figure class="connectivity-image">
	    <img
	    data-src="/assets/images/projects/connectivity/graph_circular.svg"
	    src="/assets/images/projects/connectivity/graph_circular.svg">
</figure>

And there we have it: our final graph. With this we can start asking interesting questions, such as "If we wish to protect one forest patch, which should it be?", or "If we want to regenerate some forest in the area, where should we do it in order to maximize species movement?"

## Conclusion
To maintain biodiversity, animals need to be able to move around. We therefore need to model the movement of species between forest patches. This helps us understand how and where to focus our conservation efforts.