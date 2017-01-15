villages  10,000
small town  50,000
town  100,000
city  500,000
metropolis

# Flag

Cool? Not so cool? Blank for no strong feelings.

# Easy to Extract

# Read up for Attractions

# Data items

## country

Go to Daily Program

`soup.select("div#main > ol > li:nth-of-type(3) > a > span")[0].string`

```
<ol itemscope="" itemtype="https://schema.org/BreadcrumbList">
                    <li itemprop="itemListElement" itemscope="" itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="/">
                    <span itemprop="name">Home</span>
                </a>
                <meta itemprop="position" content="1">
            </li>
                            ›
                                <li itemprop="itemListElement" itemscope="" itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="/europe">
                    <span itemprop="name">Europe</span>
                </a>
                <meta itemprop="position" content="2">
            </li>
                            ›
                                <li itemprop="itemListElement" itemscope="" itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="/ireland">
                    <span itemprop="name">Ireland</span>
                </a>
                <meta itemprop="position" content="3">
            </li>
                        </ol>
```

## Number of nights, Difficulty Level, Mileage Average, Cost

```
<aside class="tour-details">
                    <div id="detail-container" class="detail-wrapper">
                        <table id="detail-table" class="detail-table">
                            <tbody><tr>
                                <th>Type of tour:</th>
                                <td>Self-guided</td>
                            </tr>
                            <tr>
                                <th>Level <a href="#tooltip-levels" data-modal="inline"><span class="encircle">?</span></a>:</th>
                                <td>2</td>
                            </tr>
                            <tr>
                                <th>Duration:</th>
                                <td>7 nights</td>
                            </tr>
                            <tr>
                                <th>Distance:</th>
                                <td>18 Miles/day average</td>
                            </tr>
                            <tr>
                                <th>Dates:</th>
                                <td>Daily: Apr 1-Oct 15, 2017</td>
                            </tr>
                            <tr>
                                <th>Tour price:</th>
                                <td>€730 (self guided)</td>
                            </tr>
                            <tr>
                                <th>Start city:</th>
                                <td>Donegal, Ireland</td>
                            </tr>
                            <tr>
                                <th>End city:</th>
                                <td>Donegal, Ireland</td>
                            </tr>
                        </tbody></table>
                    </div>
                    <div id="tooltip-levels" class="mfp-hide">
                        <h3 class="modal-title">Level of difficulty</h3>
                        <p><strong>Tours using road, hybrid or touring bikes:</strong></p>
                        <ol>
                            <li>Mostly flat</li>
                            <li>Flat with some gentle slopes</li>
                            <li>Rolling, hilly terrain</li>
                            <li>Some long and/or steep climbs</li>
                            <li>Extensive climbing</li>
                        </ol>
                        <p><strong>Tours using mountain bikes:</strong></p>
                        <ol>
                            <li>Mostly flat, wide trails</li>
                            <li>Some gentle slopes, wide trails</li>
                            <li>Rolling, hilly terrain and/or narrow trails</li>
                            <li>Some long and/or steep climbs and/or technical trails</li>
                            <li>Extensive climbing and/or highly technical trails</li>
                        </ol>
                    </div>
                </aside>
```

## Surface

```
<section id="tour-details-11" class="expand-details large ">

                                                                                                <h3 class="detail-summary">Surface and Terrain</h3>
                                <div class="detail-content">
                                    <h3>Surface and Terrain</h3>
                                        
    <div class="self-guided">
                                    <p><span class="text">This tour goes through moderately hilly terrain. It is relaxed cycling over primarily short, rolling hills. The roads are paved small secondary roads with little traffic. The daily distances will be up to 35 miles (55 km) per day.</span></p>
<p><span class="text">While it is relaxed cycling through beautiful terrain, we do recommend being comfortable with cycling hilly terrain for a few hours each day.</span></p>
                        </div>
    <div class="guided" style="display: none;">
            </div>

                                </div>
                                                            </section>
```

## Mileage Min, Mileage Max, Number of Loops, Cities/Towns vs Villages, Attractions

Toggle Daily Program

```
<div class="accordion-alias">
                                <ul><li class="accordion-toggle">Tour Description</li><li class="accordion-toggle">Highlights</li><li class="accordion-toggle active">Daily Program</li><li class="accordion-toggle">Route Map</li><li class="accordion-toggle">Dates and Prices</li><li class="accordion-toggle">Tour Q&amp;A</li><li class="accordion-toggle">Reviews</li><li class="accordion-toggle">Included Services</li><li class="accordion-toggle">Hotels</li><li class="accordion-toggle">Bike Rentals</li><li class="accordion-toggle">Surface and Terrain</li><li class="accordion-toggle">How To Get There</li><li class="accordion-toggle">Tour Company Terms and Info</li></ul>
                            </div>
```
