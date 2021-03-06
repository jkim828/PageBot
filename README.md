# What is PageBot®?

PageBot is a page layout program that enables designers to create high quality documents by programming. It is available both as Python library working with [DrawBot](http://www.drawbot.com) and as part of a collection of stand-alone desktop applications. Other contexts such as [Flat](http://xxyxyz.org/flat) and InDesign are currently being developed. They will allow PageBot to output to print ready formats and to run on environments other than Mac OS X such as Posix web servers. The aim of the developers of PageBot is to create a system of scriptable applications to generate professionally
designed documents that use high quality typography.

- The core library, tutorial and basic examples for PageBot are available under
MIT Open Source license from
[github.com/PageBot/PageBot](https://github.com/PageBot/PageBot).
- Desktop application examples can be found in the separate a repository,
available under MIT Open Source license at
[github.com/PageBot/PageBotApp](https://github.com/PageBot/PageBotApp).
- A growing library of real document examples are bundled in Examples, available
under MIT Open Source license from
[github.com/PageBot/PageBotExamples](https://github.com/PageBot/PageBotExamples)
- A manual, generated automatically with PageBot, is at
[pagebot.github.io/PageBot](https://pagebot.github.io/PageBot)
- A website fully generated with PageBot can be found at
[designdesign.space](http://designdesign.space). It also includes entry points
for studies and workshops on how to work with PageBot.
- The TYPETR Upgrade website
[upgrade.typenetwork.com](https://upgrade.typenetwork.com) is an example where
the HTML/CSS code and all illustrations are generated by PageBot scripts.

PageBot® is a registered trademark 
U.S. Serial Number: 87-457,280
Owner: Buro Petr van Blokland + Claudia Mens VOF
Docket/Reference Number: 1538-25     

# Status

Although publicly available as Open Source under an MIT license, PageBot is
still in an alpha phase. More examples are currently being created to fully
test all functions. Issue reports and contributions are highly appreciated!

We keep track of known bugs, development and future features in the issue tracker:

 * https://github.com/PageBot/PageBot/issues
 * https://github.com/PageBot/PageBot/projects
 * https://github.com/PageBot/PageBot/milestones

## Current Functionality

Current features include:

* Various types of Element objects can be placed on a page or inside other
  Element objects.
* Grids can be defined through style measurements and views.
* Page templates (or templates for any other element combination) can be
  defined and applied.
* Automatic layout conditions for elements, for example even distribution
  across or floating down parent elements.
* Specialized views on a Document, such as plain pages, spreads and other
  layout of page groups, optional with crop-marks, registration-mark,
color-strips, file name, etc. The result of all views can be placed on pages as
illustration.
* Graphics - using all Drawbot drawing tools.
* All image filtering supplied by Drawbot ImageObject.
* Access and modify images on pixel-level.
* Cascading styles, where Element values inherit from parent Elements, similar
  to CSS behavior.   
* Text flows are using the macOS FormattedString for all typographic
  parameters.
* Random Text generator for headlines and articles.
* Read text from MarkDown and XML (.MD .XML)
* Support large amount of text processing functions:
   * centered, left, right and justified
   * Text to fit a box and elastic box to fit text
   * Tabular setting
   * Text Flow from one element to another. 
   * Variable Font UI access and instance creation, as the whole "fonttools"
     Python library is available.
   * Access to all font metrics.
   * Outline Font access modification.
   * Space, groups and kerning access and modifcation.
   * OT layout and feature access and modification.
* 3D Positioning of points, for future usage.
* Motion Graphics, export as animated .gif and .mov files, keyframing timeline, 
* Export to PDF, PNG, JPG, SVG, (animated) GIF, MOV, XML, through programmable
  views.
* Build web sites, pre-compiling all images used into the formats that can be
  displayed by browsers (.PNG .JPG .SVG)
* Automatic table of contents, image references, quote references, etc. from
  composed documents.

## Future Developments

* Element classes supporting various types of graphs, info-graphics, maps,
  PageBot document layout, Variable Font axes layout, font metrics.
* Font class supporting CFF (.otf) and UFO.
* Views for thumbnail page overview, combined booklet-sheets for print,
  site-maps, etc.
* Add export of text to MarkDown .md files.
* Add export to online documents, such as HTML/CSS/JS for specific designs of
  web pages, such as Kirby.
* Export to WordPress® PHP sites.
* Export to Ruby®/Sketchup® data files.
* Add export to Angular® files.
* Export to InDesign® and Illustrator®, as close as possible translating
  PageBot elements to the native file format of these applications.
* Time line, definition and editing, length and fps.
* Integrate the PageBot manual builder with other export functions of the library.
* Add more unit-tests to guarantee the integrity of the library and output
  consistency.
* Automatic support of ornament frames, in connection to the Element borders
  and the layout of exiting (TN) border fonts.

## Types of Publications

* PageBot stationary and publications as scripted templates
* Specimens for TN library
* Recreation of legacy type specimens as PageBot templates
* Magazines
* Newspapers
* Newsletters
* Books
* Parametric corporate identities including their styleguides, stationary and
  business card templates.
* Parametric advertizements (connecting to existing ad-systems)
* Online documents, such as single page websites
* Wayfindng templates for signs and maps
* T-Shirt templates
* Templates with embedded information for graphic- and typographic education.

# License

All PageBot source code is available as open source under the MIT license. 
However, some other separate works are aggregated in this repository for
convenience, and are available under their own licenses. See LICENSE files for
details.
