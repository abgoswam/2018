## JQuery and DOM.

I recently attended a meetup organized by [Galvanize](http://www.galvanize.com/). The meetup was about an gentle introduction to jQuery and DOM. I wanted to supplement my learnings by writing this post.

> This post is part of the series on [Getting Started and Beyond](https://github.com/abgoswam/getting-started-and-beyond)

## Topics Covered

- [Getting Started](#getting-started)
	- [HTML](#html)
		- [HTML Tags](#html-tags)
		- [HTML Attributes](#html-attributes)
	- [CSS](#css)
		- [Elements](#elements)
		- [Ids](#ids)
		- [Classes](#classes)
- [Going Beyond](#going-beyond)
	- [JavaScript](#javascript)
		- [What is JavaScript ?](#what-is-javascript-)
		- [Variables](#variables)
		- [Functions](#functions)
		- [Conditional Statements](#conditional-statements)
	- [jQuery](#jquery)
		- [What is jQuery ?](#what-is-jquery-)
		- [Invoking](#invoking)
		- [OnClick Events](#onclick-events)
		- [Adding and Removing Classes](#adding-and-removing-classes)
		- [this Keyword](#this-keyword)
	- [DOM](#dom)
		- [What is DOM ?](#what-is-dom-)
- [Misc Tips](#misc-tips)
- [References](#references)

## Getting Started

### HTML

The syntax of most HTML is as follows:

- Tags : code that wraps around the content of HTML to designate a particular effect, sometimes inherent to the tag.
- Attributes="" : code inserted into tags to implement a particular effect that is external to the tag.
- Elements - the combined syntax of tags, attributes, and elements.

`e.g. Element = <tag attribute=”blahblah”>content content</tag>`

#### HTML Tags
Tags are used to mark up the beginning and end of an HTML element.

Common Tags:
- `<html></html>` designates document as HTML
- `<div></div>` notes a block element in the page
- `<a></a>` anchor, activates a link in the page
- `<head></head>` contains meta information
- `<body></body>` contains browser information
- `<span></span>` notes an inline element

#### HTML Attributes
HTML attributes inform the browser on what to do with a tagged piece of content. Attributes generally appear as name-value pairs.

`<p class="foo">This is the content of an element with class 'foo'.</p>`

The most common attributes are:

- id="" - id is used on only a single element"
- class="" - class can be used on multiple elements"
- href=”” - hyperlink reference to an internal or external link
- src=”” - source file to an image, video, etc.
- style=”” - add some color, font, margins, etc.

### CSS

Three primary objects:

- Elements: e.g. h1, div, body
- IDs: everything that starts with a “#”
- Classes: everything that starts with a “.”

#### Elements

#### Ids

IDs are attributes that are used only on one element ONLY and noted with a “#” symbol in CSS e.g.
~~~
HTML:
<a id=”leesName”>Lee Ngo</a>

CSS:
#leesName {
    color: white;
}
~~~
IDs are used to direct functions to unique elements in the HTML so that there’s no confusion e.g clicking to a specific part of page

#### Classes

Classes are attributes something to multiple elements on a page noted with a “.” symbol in CSS.
~~~
HTML:
<a class=”ninja”>Lee Ngo</a>

CSS:
.ninja {
    color: black; margin: 10px;
}
~~~
Classes are used to change or affect multiple items in an HTML document at once . e.g. everything with class=”ninja” should have the same attributes

## Going Beyond

### JavaScript
> Sample project with JavaScript basics is on [GitHub](https://github.com/abgoswam/getting-started-and-beyond/tree/master/02-jquery-dom/javascript)

> A simple 5-min into to JavaScript [here](https://www.javascript.com/try)

#### What is JavaScript ?
[TBD]

#### Variables
[TBD]

#### Functions
Functions are blocks of code that perform tasks for us.

In JavaScript, you follow the general syntax: 1) declare, 2) define, 3) call (invoke).

Syntax:
~~~
var multiply = function(a,b){
return a * b
};
multiply(2,4);
~~~
#### Conditional Statements
[TBD]

### jQuery
> Sample project with jQuery basics is on [GitHub](https://github.com/abgoswam/getting-started-and-beyond/tree/master/02-jquery-dom/jQuery)

#### What is jQuery ?
JQuery (also called jQuery in this tutorial) is a JavaScript library initially released in 2006 and stands as the most popular JavaScript library in use today

#### Invoking
- jQuery. - the "super" jQuery object that invokes all other objects to point to your jQuery library in your JavaScript file.
- $ - is the alias for jQuery. Its appearance in a JavaScript file or an HTML script tag implies that jQuery will be used on this line and the blocks that follow.

After invoking jQuery, the syntax follows the JavaScript standard of "Define, Declare, Call". Behold, the first function you declare: "Document, Ready"!
~~~
$( document ).ready(function() {
     // insert the rest of your code here.
});
~~~

#### OnClick Events
[TBD]

#### Adding and Removing Classes
[TBD]

#### this Keyword
[TBD]

### DOM
#### What is DOM ?
The Document Object Model (commonly known as the DOM) is a cross-platform, language-independent convention that allows you to communicate and interact with elements in HTML, XHTML, and XML. Applying a tree-like structure, the DOM is essential to any training of jQuery.

## Misc Tips

## References

- http://www.galvanize.com/learn/learn-to-code/intro-jquery-dom/
- https://github.com/GalvanizeOpenSource/Learn-To-Code-HTML-CSS
- https://github.com/galvanizeOpenSource/learn-to-code-javascript
- https://github.com/GalvanizeOpenSource/Learn-To-Code-JQuery-DOM
