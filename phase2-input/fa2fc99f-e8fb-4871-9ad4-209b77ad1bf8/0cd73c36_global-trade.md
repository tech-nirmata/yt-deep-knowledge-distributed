---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 0cd73c36-ea2e-4b9a-b9cd-c6193ad4638d
source_title: "Global Trade"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:41:09 UTC
extractor: nlm_bulk_extract.py
---

# Global Trade

## NotebookLM-extracted transcript (Google's ASR + indexing)

Foreign welcome
back to this afternoon's session.
My name is Steve Redding.
It's tremendous to be here and
be part of this
amazing initiative that Matteo and
GCAP have put together.
And it's great
to meet you all today.
Looking forward to talking more
this evening over dinner and
drinks after today's session.
So what I'm going to try to do in
my session is talk now a little bit
about global trade.
Building on from Matteo's comments
this morning,
I'm sort of incredibly optimistic
and enthusiastic
about the field of international,
including both macro and trade.
As I'm sure you're all aware,
with rapid changes in trade policy
here in the United States and
other countries around the world,
international trade and
trade policy is a very exciting
part of the field of international
economics.
So what I'm going to try to
do today is roughly try
to do three things in the lecture.
The first is just to
sort of introduce some of the sort
of classic sources of international
trade data.
And so in trade, we're sort of
rather fortunate in the sense that
the historical infrastructure of
microdata has been much more
widely developed than it has in
international macroeconomics and
international finance.
And so Matteo and
the research team here at GCAP have
been amazing in kind of putting
this new microdata together.
Whereas in trade,
we've kind of already had that,
we'll have that for
a much longer period of time.
But I just tried to kind of lay out
to you what are the main sources of
data that are easily available,
what are the advantages and
the disadvantages of each of them?
And then I'm going to kind of
connect with some sort of classic
models from international
trade that many of you will have
taken trade courses.
And so you're going to be very kind
of familiar with those models.
This is a class of
constant elasticity trade models.
I'll be playing with some of the
properties of those models, showing
how you can linearize them and get
a very nice way of computing the
exposure of each country to shocks
in any other country in the world.
So the sort of linear algebra
representation of those models is
very powerful and very useful for
a number of reasons.
Then, towards the end of
the lecture, I'm going to try to
connect the material I've talked
about, namely on classic models of
international trade, with models of
international macroeconomics and
international finance.
So, as Matteo mentioned this
morning, over time there's kind of
a convergence where parts of
the international trade field now
are becoming increasingly close to
macro and international macro.
And so there's kind of a Very kind
of creative area of research at
the intersection of those two
fields where I think there's still
a lot of exciting work to be done.
And so I'll sort of talk about some
of our work where we're sort of
trying to combine some of the sort
of classic mechanisms and trade
models together with mechanisms
from international macroeconomics.
Cool.
So let's sort of dive in and
talk about sort of data sources.
You know, some of you may be kind
of aware of all of these, but I
just want to kind of lay it out for
those of you who are less
familiar with the trade data.
Maybe point to
a sort of few alternative sources
that you may not have heard of.
So modern world trade data
are pretty easily available, Very,
very widely available.
So as I'm sure many of you know,
the United nations com
trade database covers
the entire world trade.
It's compiled by the United
nations, available since 1960.
It reports trade data by harmonized
system six digit product.
So you know, there's around just
under 10,000 of those
six digit products.
Individual countries often report
data at a more disaggregated level.
So for example, the United States
goes all the way down to the 10
digit code and around 19,000 of
those so pretty disaggregate.
An example of One of
those 10 digit products might be
leather baseball gloves and mitts.
Sort of so pretty, you know,
pretty finely detailed
categories of products.
Other countries report
at a slightly higher level.
European Union I think goes down to
the eight digit level.
And so all digits after the sixth
one are specific to a country or
to a group of countries such as
the European Union.
Whereas the HS six digit products
are common worldwide.
And so the United nations com trade
database reports data at that level
of segregation for the whole world
from at least the 1960s onwards.
And so many of you will be
able to access those data directly
from United nations com trade
through your university libraries.
For example, when I was at
Princeton, Princeton University
Library had a subscription.
There is a kind of shortcut though
to kind of make the data even more
easily accessible.
For those of you who want to work
with these types of data, CEPI in
Paris have put together the Baki
trade database where they've
essentially cleaned up the United
nations com trade data for you.
So at least for recent years, so
you know, the most easily usable
Data is from 1995 through to 2023.
They've actually taken all
the years of United nations data.
And importantly, because year to
year or occasionally every certain
number of years, the harmonized
system changes the exact definition
of products can change as new goods
get created, like the iPhone and so
on, or the revisions to
the existing set of goods as some
goods are no longer relevant.
The exact classification changes
over time.
And so CEPI has kind of made things
easy for you by mapping goods
between those classifications.
And so the data are available
According to the 92, the harmonized
system 92 classification on
a consistent basis
all the way from 1995 to 2023.
And then if you're only
interested in shorter time frames,
they also report data using later
years of classification.
So for example,
96, 2002, 2007 and so on.
So that's a really great resource
if you really want to be able to
have data
on trade between many countries
at a finely detailed product level.
One limitation of those data sets
though, of course, and
I want to emphasize that now
because this has been important in
trade in recent years,
is there's not much information
at the firm level about individual
firms importing and exporting.
So if you're interested
in sort of matching and searching,
matching between buyers and
sellers, these data
are not going to be as suitable.
And I'll say more about
sort of alternatives if you really
want the firm level information.
But nonetheless, you know,
really great source of data for
studying changes in comparative
advantage over time.
If you want to go the kind of much
longer historical time periods,
there are some other data sets that
you may want to consider.
So cepi again in Paris has what
they call the Gravity Trade
database, where if you're only
interested in aggregate country
level trade, you can get the data
all the way back to 1948.
So you can do really
long term analysis of trade policy,
how it affects patterns of trade.
So for example, Keith Head and
Thierry Mayer have a paper
on colonial linkages and
how those linkages abate over time
as countries become independent.
So again, if you.
But there the limitation is it's
only aggregate trade between a pair
of countries, you know, US, Mexico,
in a particular year, the aggregate
value of that bilateral trade, and
then those data reported for
all other bilateral pairs.
That source though is also
convenient because they've done
the work of combining those trade
data with a lot of the standard
variables you might want to
include in a gravity equation.
So as I'm sure you're all familiar,
a whole class of trade models
predicts a gravity equation for
bilateral trade flows.
I'll say more about that later.
Often when we model trade,
we're going to regress bilateral
trade on import of fixed effects,
export of fixed effects, and
then some measure of bilateral
friction such as bilateral
distance, common border and so on.
And so the CEPI gravity database
has all of those characteristics,
various different measures of
distance, proximity,
colonial relationships,
political relationships, language,
relationships between countries.
If you want to do history and
disaggregated products,
there's kind of a third source
to think about,
which is the NBER World Trader Base
Trade Database that was put
together by Rob Feenstra, released
an NBR working paper in 2005.
And so the caveat with this
data set, it's got big advantage.
Big advantage is it goes all
the way back to 1962.
The big caveat or disadvantage is
it stops in 2000, although Feenstra
has maintained some later
versions of the paper of the data.
And if you reach out to him,
he'll often give it to you.
But the sort of official data from
the MBR finish in the year 2000.
Okay. So if you're interested
in any of those databases.
These slides have active links, so
just click on the brown link.
It's going to take you
straight to the data source.
Final sort of pointer again for
kind of long term data on bilateral
trade between countries.
The IMF Direction of
Trade Statistics DOTS database also
goes back to 48.
It's one of the official
databases that the gravity,
the CEPI Gravity database I
mentioned earlier draws on.
They include the DOTS data and
then also some other sources of
long term trade data.
Okay, so those are kind of some of
the leading sources of modern trade
data for those of you who want to
get detailed information on
bilateral trade between countries,
potentially down to the product
level, to think about sort of
patterns of comparative advantage.
Often when we kind of write down
trade models, you want to go
a little bit beyond that though.
We want to sort of think about
input output linkages in
the economy because, you know,
one of the big limitations of trade
data is that they're reported
on a gross basis.
So when the iPhone is imported
from China historically into
the United States, the good value
at the border is the value of that
iPhone as it crosses the border.
Obviously not all of the value
added in that
iPhone was created in China.
The point of final assembly, some
of the chips may have been made in
Japan or elsewhere in factory Asia.
So a big limitation of the observed
trade data is their gross flows.
They don't break out
the whole value added chain.
And often when we write down models
because kind of interested in
global value chains,
input output linkages and so on.
So for those of you interested in
kind of bringing that information
in, there are sort of two main
ways in which to go.
One way in which to go is to sort
of take the gross flows data that
you see reported and then feed it
into a model that explicitly models
those input output leakages.
And so a classic example is sort of
Caliendo and Paro in the Review of
Economic Studies studying
the welfare effects of the North
American Free Trade Agreement.
And so now people in trade
have done a pretty good job in
putting together comprehensive
input output databases for
many countries around the world.
So probably the most commonly used
database is the wih,
the World Input Output Database.
That's for example used by
Arno Cosineau and Andres Rodriguez
Claire in their handbook chapter on
quantifying trade policy.
So that's going to give you
input output matrices for
43 countries and the rest of
the world data reported 56
countries using the International
Standard Industrial Classification.
So sort of standard classification
of production industries
maintained by the oecd.
It's going to be more Aggregated,
substantially more aggregated than
the trade data I talked about.
So here we've only got 56 sectors
that is going to enable us to
model those input output linkages.
There's also another
source of input output linkages,
the AORA Global Supply Chain
database, which when you first hear
about it, it sounds amazing.
It sounds really exciting.
So, you know, intersectoral flows
around 15,901 sectors across 190
countries from 1990 to 2022.
Sounds amazing until you realize
that most of the data
are actually imputed.
So, you know, there's a big kind of
health warning with this database.
But nonetheless that's a sort of
another source where
people have tried to put together
the data on input output matrices.
But it's really worth reading
the fine print and the footnotes as
to what's actually data and what'
and how the imputation's been done.
So that's one way you can go to try
to build in global value chains is
actually use the model
to model the output linkages and
feed in the input output matrix.
The other way you can go is of
course to try to sort of transform
the data, construct trade and
value added.
And so Robert Johnson, Dr.
Dame, is perhaps one of the sort of
leading people who sort of
pioneered that approach.
And there's a.
The OECD maintains the database on
trading value added, the TIVA
database, which again, you can
download from the brown link here.
Again, there are some sort
of caveats.
And what is the caveat?
Well, how do we go from gross trade
flows to trade in value added
when we don't see separate input
output tables for each importer
with each of its exporters?
Typically each importer just has
a single input output matrix
like we see in the world input
output database.
Well, the only way we can do that
is by making a kind of
proportionality assumption.
And the sort of typical assumption
is that when a country exports,
it's using the same input output
structure with all of the partners
that it exports to.
And so again,
there's kind of a big caveat there
and in some sense that should be
closely related to just modeling
the input output structure in your
model rather than just using
the trade and value added data.
But those of you who are kind of
interested in directly measuring
trading value added, that's one of
the sort of most kind of
comprehensive attempts, attempts to
correct the gross flows trade data
to deal with global value chains.
Okay, so that's one side of
international trade is the kind of
the actual flows between countries.
But obviously one of the things
trade economists are interested in.
And it's particularly
policy relevant these days
here in the United States
is thinking about trade policy.
And obviously by far the most
prevalent trade policy
is import taxes or tariffs.
There are several different sources
of those data for research.
The original kind of
meta source for all of them is
the United Nations TRAINS database
Trade Analysis Information Systems
Database, which reports tariff data
by country, partner and
product according to the Harmonized
system six digit level.
So again, same level of
classification as the United
nations com trade data strength of
the TRAINS database is it actually
reports both the most favored
nation tariff for a country.
Well, I'm not going to pick
the United States,
maybe a bad example here given
recent changes in trade policy.
But say for
Canada, it reports Canada's most
favored nation tariff.
So that's the tariff that's agreed
to under the terms of
the World Trade Organization and
that it offers to all of its
trade partners.
But then often countries, and
Canada is a good
example historically,
often may sign free trade
agreements with specific partners.
And so there will also be some
preferential rates.
And so free trade
agreements allowed as an exception
under the World Trade Organization.
And so until recently there
were no tariffs on US Canada trade.
And so the preferential tariff
would be zero on US Canada
trade historically.
And so the TRACE database reports
both the most favored nation and
the preferential tariffs.
So good example here of why
you should always look at
data when you use it.
You know, these big
databases are very sort of
intimidating just because of
the number of observations.
But you know, Fyodoro Teti, who was
a postdoc at the University of
Munich, just recently spent a year
at Princeton, she kind of pointed
out this sort of major flaw with
a lot of people who've been using
the United Nations TRAINS database.
So what's that major flaw?
Well, the most common window
through which people access
the TRAINS data is this
World Integrated Trade Solutions
database, the WITS database
maintained by the World Bank.
And as I mentioned, Trains has both
the most faded nation tariffs and
the preferential tariffs.
But the sort of footnotes or
the sort of things
some people hadn't noticed is that
countries don't always report
the preferential rate every year.
And so if you were to look at
the data reported, say for Canada
and the US in some years when
the preferential rate is reported,
the tariff would be zero because
it's a free trade agreement.
Historically until recent times,
and then in the years when
the preferential rate wasn't
reported, nothing was reported.
And so people were just sort of
imputing the most
favored nation rate.
And so unless you sort of take
account of the fact the
preferential data are only reported
in some years, if you don't realize
that you can end up with these sort
of sharp tooth shaped measures of
tariffs over time.
And it's a fun example.
Those of you who want to look at
Theodora's paper, she mentioned
some really influential papers in
the trade literature where
the tariff data was just one input.
It wasn't the focus of the paper,
but where it was subject to this
sort of missing data problem and
false imputation.
And so
Fyodora actually has sort of taken
the United nations trains database,
and she dealt with that issue,
sort of recognizing that the.
Preferential rates are not reported
in every year and she's made
available the database to you.
So for those of you who want to use
tariffs around the world,
it's kind of really important
to use Foadora's database or to
clean up the WITS data by yourself.
At least be aware of this issue
with the trade policy data.
This is not trivial.
So Fyodora finds when you sort of
re estimate the specifications in
some published papers,
you find that
the trade elasticity changes quite
noticeably when you use the correct
tariff data rather than the falsely
interpolated tariff data.
So, so good example in science,
always useful to look at the data.
It's easy to say that, difficult
to do when you have vast databases,
but it's a great example of where
just looking at the properties of
the data can be super informative.
One of the features about trade and
production is sometimes you have
production data reported
according to one classification.
So in North America that will be
the NAICS classification, the North
American Industry classification.
But then your trade data
may be reported at a different
classification, as I mentioned,
typically reported according to the
harmonized system classification.
So there are some great public
goods out there in international
trade, which I just wanted to kind
of make everybody aware of, if you
didn't already know about them.
Peter Schott's website at Yale,
he has a number of very useful
concordances, both for different
versions of the harmonized system
classification over time.
As I mentioned,
it changes over time and then also
between things like the NAICS
classification and the harmonized
system classification.
And obviously if the mapping is one
to many, it's often very easy to
put those concordances together.
But sometimes there can be many to
many mappings which are kind of
very complicated to deal with and
you have to make
various alternative assumptions.
And so actually being aware that
there actually are these standard
resources out there that can at
least provide a starting point and
help you save a lot of time
can be quite useful.
As well as Peter's website,
there's another website maintained
by the Forum for Research
in Empirical International Trade.
They organize several empirical
trade conferences each year.
So those of you who
are working more on the trade side
of international
I definitely recommend those
empirical trade conferences.
I attended them many times myself
and learned a lot, benefited
greatly from attending them.
So that's sort of one
call out for them.
And in addition
their website also has a number of
other useful concordances and
other links to data.
So just to sort of flag that as
trade researchers,
as one of the issues we have to
deal with is potential
different Classifications in trade,
of trade and production data.
And then finally,
because in some of my work I've
tried to use historical variation.
Why? Because often when you look
back in history,
there may be a natural experiment,
there may be an exogenous shock,
which actually helps shine light on
a particular economic mechanism
you're interested in.
And so actually using that
historical time period gives you
the exogenous variation you're
looking for to try to pin down
the things you're interested in.
And so I just wanted to mention
that with digitization, the fall in
the cost of computing power,
it's now increasingly available
to be able to get hold of
data on historical trade flows
a long way back in time.
So these are the sort of three most
widely accessible
historical trade databases.
There's a Federico Taina World
Trade historical database, so
focuses on the period 1800 to 1938.
So obviously the main limitation
there is it sort of stops before
the Second World War, but it gives
you historical coverage and
the data are reported by the sort
of polities at that point in time,
country boundaries at that point in
time, which obviously in some cases
quite different from
modern country boundaries.
Perhaps the best source of
historical trade
data is again from CEPI in Paris,
the TRADHIST database.
So that reports data on a sort of
consistent basis for 188 years from
1827 all the way through to 2014.
So that gives you really,
really long horizon trade.
Some great examples of papers that
have used that in creative ways.
Jim Feyrer has a really nice paper
on the Suez Canal, looking at
the closure of the Suez Canal
during the Arab Israel war in
the Middle east and then some other
work on the Panama Canal and so on.
So with that historical time frame,
you get these sort of
dramatic changes in the structure
of trade you can potentially use
to estimate the effect of trade
costs on trade flows and so on.
Look at the speed with
which adjustment occurs.
So the sepia tradition is
probably your best bet if
you want to go really back in time.
There's also a competitor to
Federico Taina, the so
called Ricardo trade database,
which again has data but just for
a historical period.
So just some sort of shout outs
there about various possible
sources of trade data for
those of you who want
to do empirical research
connecting with trade data.
So anyone got any questions
there about the data?
Just before I sort of get a little
bit into the main meat
of the model, I just want to spend
a little bit of time
outlining those sources for anybody
happy to take any questions.
Let's talk more later.
Yes, so If I'm interested
in non tariff trade arrears,
there is no great question.
So yeah, measuring non tariff
barriers for obvious reasons is
extremely hard to do.
The data are limited.
The TRAINS database does actually
have some information, so
sometimes it has data on for
each product, what are the number
of non tariff barriers or like
an indicator variable for whether
there is a non tariff barrier.
So people sometimes calculate
things called coverage ratios,
which are things like within this
two digit sector,
what fraction of products have
some form of non tariff barrier or
what fraction of trade values have
some form of tariff barrier.
And obviously the issue with trade
values is they're affected by
the barriers and so on.
But yeah,
it's hard to do but Trains has some
information on that.
For individual countries,
people sometimes try to estimate
the ad valorem equivalence of
the non tariff barrier.
That's obviously what conceptually
you want to do in terms
of a trade model.
But that sort of typically requires
more information to do that.
So if you want to get information
on many countries on non tariff
barriers, the TRAINS database is
one of the best places to go or to
sort of drill down to things like
the Multi Fiber Agreement where if
you're just interested in textiles,
you might be able to get more data
on the details of quotas and so on.
Cool.
Awesome.
So that's pretty much what I wanted
to say, almost what I wanted to say
about trade data.
Final thing I just wanted to
mention is for those of you who are
interested in the United States,
as I said at the beginning,
there have obviously been large
changes in recent trade policy.
It's quite sort of exceptional to
have such large changes in tariffs
from a relatively low level
in such a developed country.
And so with the tariffs introduced
by the first Trump administration,
there have been a whole bunch
of papers
that have used the impact of those
on various outcomes of interest.
So Pablo Fagobaum, Penny Goldberg,
Patrick Kennedy,
Andermit Kandarwal,
have a really nice paper in the QGE
on the return to protection,
looking at the sort of welfare
impact of those tariffs in
a general equilibrium trade model.
Related to the model I'm going to
develop in the lecture later today.
I've done some work looking at
the price effects of those tariffs.
And then a whole bunch of people
have looked at input
output linkages,
global value chains and so on.
Often those papers have replication
data sets available.
So for example, my papers, you can
download the replication data sets
and then you've got the combined
trade and tariff data for
the US and I think in our paper,
in the AA papers and proceedings,
we go from sort of 2016 all the way
through to October 2019,
shortly before the COVID pandemic.
I'm sure there's much more
work still to be done on trying to
understand features of
those Introduction, tariffs.
I'll say a little bit more about
that later in the lecture.
And then, obviously, in the second
Trump administration, we've seen
a further change in trade policy.
There are several papers out there.
Some of you may be aware of people
starting to analyze those data.
The trade data are reported with
a lag, so often the data
don't arrive for a few months.
And so we're sort of still waiting
for the data to come in.
And one of the challenges with
these recent rounds of tariffs
is that even when announcements
have been made, there's obviously
a lot of uncertainty as to.
So how long those tariffs are going
to remain in place for?
There's often been a 90 day pause
and there's negotiations
between countries.
And so it's not just the level of
protection changing, but
also a change in uncertainty.
And so just to flag that, again,
continuing to think about
the US As I mentioned earlier,
a limitation of the United nations
com trade databases and the other
ones I mentioned is they don't have
firm level identifiers, they don't
tell you anything about the firm.
So you can look in a rich detail
at country comparative advantage
across products.
But it's hard to do
anything on firm heterogeneity.
Think about models of heterogeneous
firms and trade and so on.
Those of you interested in working
with the type of data which gives
you firm level trade information
in the United States, the gold
standard is the Linked Firm Trade
Transactions database, which is
available from the Census Bureau
requires you to have access through
a census research data center.
And so those of you who
are interested in working on
the United States having the firm
information, that's the way to go
is to put in a proposal.
Anyone can submit a proposal.
It can take up
to six months to get approved.
So it's good to do it
earlier rather than later.
The way that proposals are judged
is in terms of enhancing census
ability to fulfill its mission
to monitor the American economy.
So when you write your proposal to
access the data, it's not enough
just to talk about why your paper
is economically important
because you're testing a model or
testing a key hypothesis in trade.
But it's also worth making clear
how your research project
is going to help the census learn
more about the American economy,
because that's ultimately
the Census Bureau's mission.
So just to kind of flag that for
those of you interested.
And then if you don't want to go
the Linked Firm trade transactions
database, you don't want to go that
route because of the sort of delays
and so on.
There are a couple of other options
out there and
I just want to mention them and
again, their limitations,
not everyone's aware of them.
There is a whole bunch of
alternative sources for what's
known as bills of lading data.
So when goods are loaded on a ship,
a bill of lading is completed,
that tells you who's the shipper,
who's it being shipped to,
what the product is,
what port does it go through,
what the mode of transport is,
and so on.
Those data are pretty easily
available from private companies.
So Data Mine
is one of the leading companies.
Panjiva is One of the other
leading companies.
The big caveat,
not everyone's aware of this,
is that those data do contain trade
values, but they're imputed.
And so at least in the United
States, in the United States,
the values of the transactions is
confidential information.
If you want the true values,
you have to apply through
the Census Research Data center,
as I mentioned.
So how does Pantiva come up, or
data mine come up with values?
Well, they essentially impute them
based on the public data.
So they know that the Census Bureau
reports the total value of trade
for each product, it reports
the total value of trade for
each country, and so on.
So you have various sort of
aggregations of the microdata, and
you can use those aggregations,
feed them into an algorithm, and
try to predict what
the unobserved trade value is.
And so just to kind of, again,
you should kind of know that and
be aware of that if you want to use
those data.
For some countries,
Pangeva actually does have
the reported values.
So I believe in Mexico, the bills
of lading actually do contain
the true values that are the same
as the official customs values, but
for most countries,
they're impeded.
So again, just.
Just to flag that.
Okay, cool.
So now I'm going to start
transitioning to the.
Yep, on that point.
Historical bills of lady data.
Great question.
So I guess in principle there
are things like that.
So Britain is
the country I know best.
So there are customs ledgers
that record imports by product,
by country that are all like
handwritten for Britain.
There are also portbooks for
individual ports in Britain that
tell you which ship came in, what
it contained, typically lists for
each ship, or the main items
included in the shipment.
It's not going to be as rich as
the modern bills of lading data,
but it's something like that.
And most countries have some form
of historical ledger like that.
It varies by country.
What exactly is recorded.
It's typically recorded in
handwritten once you get back to
the sort of 1800s and so on.
But related to Melissa Dell's talk
tomorrow, there are now increasing
algorithms enabling you to kind
of digitize handwritten records.
And, you know, if we go closer to
the modern day,
there probably at some point were
also printed bills of lading.
But it's just a question of how
many of them have survived, like
digitally for the United States.
I'm not aware of anything before,
I think like the late 1980s,
early 1990s, that's the longest you
can go back in the digital data.
And I'm not aware
of any sort of printed Forms.
Before that it could be there lying
around in a warehouse somewhere,
but I've not heard about them.
But yeah, it's a great question.
So now I'm going to transition
a little bit to the sort of main
meter of what I wanted to talk
about today, which is to kind of
connect with the classic set of
models of international trade that
many of you will be familiar with,
so called Constantine Sicily trade
models, and then showing them
how you can use them to construct
these sort of rich measures of
the network of trade and
countries networks of exposure
to shocks in other nations.
So all the code and other resources
for everything I talk about today
is going to be available online.
So the main code is on
this website here,
internationalfriendsandenemies.com,
you can also get it from my
webpage.
It has the replication data
and code.
It also has a whole bunch of
interactive maps and
network graphs.
So you can actually
graph the network of world trade,
how it evolves over time,
pick your country of interest,
your year of interest and so
on in an interactive way.
And then I'll also connect a little
bit later to a subsequent paper
where we kind of combine
the trade model that I start with
some dynamics.
And I'm going to be talking about
some dynamics later in the lecture
today, again on my website.
I have a replication archive for
that paper as well with all
the code.
And because the dynamic model is
a little bit involved to make it
particularly easy to use these
techniques, we also created a model
toolkit which is essentially
creating a Monte Carlo of a little
simulated model economy and
then showing you how to implement
our code for that model economy
in a way that's as transparent as
possible to make it as easy as
possible to use these techniques
for characterizing the transition
path in dynamic models.
Okay, cool, cool.
So let's get
into the main meat of the lecture.
So I'm going to begin by talking
for about half of the remaining
time about this paper,
international friends and enemies,
which are going to connect with
the sort of standard classic trade
models you're all familiar with.
I'll show you how we can construct
these measures of
the network of trade.
And then in the second half of
the remaining part of the lecture,
I'm then going to show you how we
can take one of those models and
combine it with an international
macro model and
try to connect the trade flows,
the mechanisms you think about in
trade, with some of the classic
mechanisms people in international
macro are interested in.
Try to kind of connect these two
fields together with one another.
And in that second part of
the lecture, I'm going to be using
some of the CPIS data that Antonio
mentioned earlier, and
I'm going to be building on
the GCAPS restatement of the data
from residency to nationality.
All of that's going to be kind of
feeding into the model.
And this paper I'm going to talk
about first is joint with
Ernest Liu and Benny Kleiman.
And the paper I talk about later
will be joined with them and
then also Moto Yoga.
Cool. So what
was the motivation for this paper?
Well, we were sort of really
interested in this debate
about geopolitics, which is part of
this year's session and gcat.
So thinking about the idea that
when you look around the world, you
see major changes in the relative
economic size of countries, they're
often accompanied by major shifts
in the balance of political power.
So obviously thinking today
with the rise of China,
there's a lot of informal
discussion of China gaining
increased political influence over
countries through the Belt and
Road Initiative, through its
trade linkages with countries,
particularly in Sub Saharan Africa
and in other emerging economies.
If you look back in
time historically,
people also talk about the conflict
between Britain and Germany towards
the end of the 19th century,
beginning of the 20th century.
As another example of where
an initially large country,
Britain, was faced by an emerging
challenger, Germany,
rapidly becoming of similar size or
even bigger size all the time.
And so I want to kind of think
about that idea that changes in
the economic size of countries
might be accompanied by shifts
in the balance of power.
So in order to think about
that question, I'm going to need an
economic measure of how dependent
is my country on another country.
And so that's where we're going
to use this class of constant and
elasticity trade models to try to
provide exactly a micro founded
rigorous measure of the extent
to which I'm economically dependent
on another trade partner.
So we're kind of interested in
a hypothesis that as countries
become more economically dependent
on a trade partner,
do they realign politically towards
that trade partner?
The sub Saharan African countries
have become more dependent on China
for trade and their growth.
Have they started to vote in
similar ways of China to support,
to form political treaties with
China to become more closely
aligned politically with China?
And obviously that's a challenging
question to answer for
a couple of reasons.
Well, one is, well,
how do you measure how economically
dependent one nation is on another?
I can't just look at the bilateral
trade flow because that's a sort of
partial equilibrium measure.
How to dependent on one country
depends upon what my outside
options are, what the choice set
is, and how much I trade with other
countries in that choice set.
And so I need to think about in
general equilibrium, I need to have
a measure of dependence that's
consistent with general equilibrium
in a class of trade models.
And so that's one of the things
we're going to try to do.
So we're going to say that
a country is an economic friend
of its trade partner if
growth in that trade partner
raises the country's income.
And the country is going
to be an economic enemy if growth
reduces its income, that might
be nominal income or real income.
We're going to be most interested
in real income as a measure of sort
of welfare exposure.
So how dependent is my welfare to
growth, growth in China?
And we're going to see how to
compute that in a rigorous way
in class of generally
equilibrium trade models.
Obviously another challenge here is
when you think about that question
of as a country
becomes more economically dependent
on a trade partner,
does it realign politically?
One other kind of challenge I'm
sure you're all thinking about
is obviously causality as well.
Right?
So it could be that
as I become economically
dependent on a country,
I politically align with it.
The causality
could run the Other way, maybe for
some exogenous reason, there's
a political salience between
our two countries and that leads
us to trade more with one another.
And so obviously reverse causality,
or more generally,
omitted variables that might both
affect trade flows and
political alignment are going to be
a cause for concern.
And so that's also something we're
going to try to take seriously, and
we're going to try to use the model
to help us construct instruments.
So we're going to be using kind of
ideas of
model based instruments to also try
to help overcome that challenge.
How are we going to measure
political alignment?
Well, we're going to use
a bunch of measures.
We're going to use voting in
the United Nations.
Do countries vote in similar ways
in the United Nations?
We can use various different ways
of coding that.
We'll also use measures of
strategic rivalries,
which is where political scientists
directly measure whether they think
one country is a source of threats
or an explicit enemy of another, or
engage in conflict with another.
And then we'll also use direct
measures of formal alliances.
So have we signed an agreement?
What type of agreement have we
signed with one another?
And to try to use those, and
to try to see whether our results
are robust across different ways of
measuring political alignment.
Okay, so more formally,
how are we going to model this?
Well, we're going to think about
countries being able to undertake
political actions that raise
the productivity of their trade
partners, but
that incur utility costs.
So I can vote in a way
that's favorable to your economic
development in the United nations,
or I can agree to a treaty that's
beneficial for your economic
development that incurs some
private utility costs to me.
And so why am I going to be willing
to do that?
Well, I'm going to be willing to do
that if adopting this favorable
policy to you that raises your
growth and enhances my welfare.
And so countries are essentially
going to trade off the private
utility costs of undertaking
favorable political actions against
the economic gains from taking
that action, raising the growth in
their trade partner and thereby
increasing their own welfare.
I'm going to use a trade model to
measure that economic dependence,
the impact of growth on my welfare.
So what are we going to use for
the two instruments I mentioned
to overcome
the challenge of endogeneity?
Well, we're going to use two
different sources of
quasi experimental variation.
So the idea here is if we
find similar results with two
very different sources of quasi
experimental variation, then other
things equal, that might enhance
the credibility of the empirical
findings because those instruments
are using very different sources of
variation in the data.
So we use a model based instrument
based on China's emergence into
the global economy.
So building on the idea that Walter
Dawn Hanson and many others in the
trade literature have explored that
China's domestic reforms in 1978
were a shock to other countries
because they enhanced its growth,
led to an expansion in trade, and
that then impacted other countries.
So that's going to be our
first instrument derived within the
structure of the model, and I'll
explain that a little bit later.
And then our second instrument,
we're going to use an idea from
James Feyre, from a second paper by
James Feyrer, which is that over
time the share of trade by air has
increased dramatically.
Does anybody know what sheriff
to exclude Canada and Mexico?
Anybody have a guess what share of
US imports is by air?
By value?
Anyone have any sense?
2%?
80%?
Anyone want to hazard a guess?
50%.
Which is pretty amazing, right?
That's by value
rather than by weight.
So by weight,
obviously most stuff comes by ship.
But by value, if you exclude Canada
and Mexico, around 50%
of US imports comes by air.
And if you go all the way back to
the 60s and even before the early
days of jet travel, that share of
airship was obviously much,
much smaller than today.
What's the idea?
Well, the invention of the long
distance airplane reduced trade
cost differentially for countries
that have long sea distances
relative to air distances.
So if you look at the position of
the land masses on the globe,
they generate a lot of variation in
sea distances because ships
have to sail around the coasts
to go from one port to another.
And so when there's a new
innovation like air travel, where
I can fly great circle distances,
essentially I can fly point to
point, follow least cost paths.
That's going to unevenly reduce
trade costs depending upon
the extent to which countries have
long sea distances
relative to their straight line or
great circle distances.
And so that'll be our
second source of variation.
What do we find?
Well, we find that increases in
my economic dependence on a trade
partner predicted by our
instruments and indeed lean towards
political realignment.
We find that's very similar
estimates across these two
very different sources of quasi
experimental variation.
And we find that using our theory
based measures of economic
exposure is kind of consequential.
If we just use a simpler measure
like bilateral trade,
we do not find the same thing.
So actually using the model and
the model's based measure is sort
of informative.
Okay, cool.
So then obviously, you know, this
connects with a rich literature on
international political economy and
recent work on GE economics,
including Matteo and Antonio and
Chris's work, about which they're
going to be talking later
as part of part of this course.
So how are we going to measure this
generally clearer
measure of economic dependence?
Well, we're going to take
the standard class of
continental assisted trade models.
So I'm sure many of you are aware
in international trade, there's now
a whole class of models.
What defines this class of models?
Well, essentially, they all imply
a gravity equation for tray flows.
In which there's
a constant elasticity of trade
flows with respect to trade costs.
And I'm going to develop one of
those models here which is perhaps
the simplest model in that class.
And that's the so
called Armington model of trade
where goods are differentiated by
country of origin.
So in other words,
German goods are different from
French goods, horizontally
differentiated from one another.
But within Germany
markets are competitive.
Many firms can
produce the German good.
One unit of the German good is
the same as any other
unit of the German good.
But it's just the German good is
different from the French good.
That seems like a very bare bones
model of trade.
It's actually a model quite often
used in international macro.
So it's kind of nice to see
it in terms of bridging the gaps in
international macro.
Macro often works with Armington
models, but essentially there's no
loss of generality here because
instead of this Armington model of
trade, we can derive exactly
the same predictions from
The Eaton Cortem a 2002 Ricardian
model of trade in which trade is
driven by technology differences
across goods and across countries.
As long as technology is random and
drawn from an extreme value
distribution, a fresh
a distribution that's going to
give us exactly the same system of
generally flipping conditions that
I'm going to outline in a second.
So that's another
model in the class.
So Armington
goods are differentiated by origin.
Ricardian model,
technology drives trade.
What's another model
within this class?
Krugman 1980.
So the Krugman 1980 model in which
firms make differentiated varieties
under conditions of monopolistic
competition and increasing returns
to scale, it turns out that that
model also falls within this class.
And fourth example of a model
within this class, the Mellets 2003
model affirm heterogeneity
in differentiated product markets.
If productivity is Pareto
distributed, then again it's going
to fall within this class of
Constantine trade models.
Why are we so
obsessed with this class of
constant density trade models?
Well, in particular
it does a good job at hitting one
key moment in the data.
It explains why
the gravity equation is
extremely high predictive power for
bilateral trade flows.
So in other words,
if you regress bilateral trade
between countries on exporter fixed
effects, importer fixed effects and
just geographic distance.
So something incredibly simple.
You think it's too simple to have
much explanatory power in logs that
has an R squared of around 0.8
a lot of predictive power.
If you estimate it with something
more sophisticated like a Poisson
pseudo maximum likelihood
estimator to allow for
zeros that also provides a good
approximation to the data.
And so this sort of
constant elasticity relationship is
obviously not going to be perfect,
but it's going to provide
a good approximation to the data.
And that's why this class of models
is so widely used.
And so we're going to
take that widely used class and
show it how you can derive this
rigorous measure of the extent to
which my welfare is dependent on
growth in a trade partner.
So let's walk through that.
So what's
our assumption about preferences?
Well, we're going to think
about countries.
Preferences are defined over these
horizontally differentiated goods
produced by each nation
around the world.
And then they take the constant
illicit substitution for.
So I've written here
the indirect utility function.
So the utility function in terms of
wages and prices, so the wage in
the numerator and the denominator
is the ideal price index.
It's the cost of living for
a constant elasticity of
substitution demand system.
So I'm just summing
this is utility in country N
summing across all exporters I
saying that's important.
I'm using the Eaton Corton or
Costa Sarcophakis notation.
The first subscript is
the importer, the second subscript
is the exporter.
So a price index depends upon
the sum across all exporters of
the price they charge to import N
raised to a power and that power is
1 minus sigma where sigma is
the illicitious substitution
between these countries goods.
And I've just defined theta as
sigma minus one and then written
the price index where the exponent
on price is is minus theta.
And the reason I've done that is
going to be obvious in a second
because theta is going to be
the trade elasticity.
The elasticity of trade flows with
respect to trade costs is going to
depend upon sigma minus one.
So what's the feature of the CES
demand system?
Well, as we know it gives
us these nice constant elasticity
expressions for expenditure shares.
They take the sort of logit or CS
form where the expenditure share s
of importer N on exporter I depends
upon the price that exporter I
charges in market N relative to
the price charged by all other
exporters where the prices are
raised to a constant elasticity.
So you know, strong assumptions for
those of you interested in IO at
all, if anybody here's on the IO
international macro boundary, which
may be a small set, but the strong
assumption here is independence of
relative alternatives.
If I look at relative expenditure
shares for two exporters,
it just depends upon the relative
prices not upon the price of any
third of the country.
How about the production
side of the model?
Well, simplest possible
production slide,
goods are produced with labor.
So W is the wage.
Linear production technology,
constant returns to scale.
We're going to allow our
countries to differ in terms of
their productivity Z and
countries are going to face iceberg
bilateral cost of trade.
So if I want to ship from country I
to importer N, I have to ship tau
ni units of the good in order for
one unit to arrive.
So tau is a measure of the iceberg.
So Tau -1 melts in transit, I ship
Tau greater than one unit and
one unit arrives.
So if I substitute that pricing
rule into my expenditure share now,
I see immediately this constant
elasticity gravity equation,
bilateral expenditure shares,
the share of expenditure of country
N on country I depends upon
bilateral trade costs tau ni.
So if I think trade costs increase
with distance, that's going to be
what explains in the data
that I see, distance declines,
trade flows decline with distance,
roughly with a constant elasticity.
But we also see some kind of
another very important insight of
the model, which is that it's not
just bilateral trade costs
that matter for the trade
between importer N and exporter I.
Importer N's trade costs with all
other exporters M also matter
because they're in the denominator.
Here. If I substitute for
PNM using my pricing rule,
I see that it's not just
bilateral trade costs between N and
I that matter for their trade.
It's also multilateral trade cost
or multilateral resistance,
the trade cost with all other
nations, in other words,
Australia and New Zealand,
they're a long way away from one
another, but they trade much more
with one another than you think
based on their distance.
Why? Because they're
miles away from anywhere else.
And so it makes my relative prices
that matter for trade flows.
And that's one of the key insights
of these models,
what's called structural gravity,
that you need to take account of
those price index effects.
Okay, and so what's so
elegant about this class of models
is that the general equilibrium of
these models reduces down
to a single system of equations for
the N countries.
So the systems
defined across the N countries, and
the only unknown is going to be
the wage, or the only kind of key
endogenous variable is going to be
the wage of each country.
Okay, so what does this system of
equations equate?
It says that income in each country
of production, which is paid out to
labor with zero profits, the wage
times the labor endowment income in
country I has to equal expenditure
on the goods produced by country I.
So that's just the sum across all
markets n of income in each market
multiplied by the share of
expenditure the market N
spends on I.
And if we substitute our
expression for
shares into that income accounting
equation, and if we substitute for
the pricing rule in prices, we're
going to see that we can reduce
that system of equations down to
a system in the vector of wages
in each country around the world.
So the actual only unknowns in this
general equilibrium system.
Other wages in each
country around the world.
I'll say more about that in
a moment when I'm going to be sort
of solving for
the impact of productivity shocks.
I'm going to need to pick
a numerator.
I'll typically pick the numerator
that world GDP is equal to 1.
And just for
sort of future reference
I'm going to define Q as income.
So wages times
the labor endowment and so
the sum of Q across all countries
around the world equals one is
going to be my choice of numeraire.
And you'll see why
that's convenient in a second.
Okay, so now let's look a little
bit more about that
general equilibrium.
So now I've made the substitution.
We see the system of equations and
the end wages in each country.
And you know what's nice about this
system of equations is it's really
just an excess demand system.
Right? Well what is
the demand here?
It's the demand for countries labor
and the price here is the wage,
the price of labor in each country
around the world.
And this excess demand system
satisfies gross substitutes.
So if I increase the price of
the good produced by country I,
that's going to reduce expenditure
on country I and increase
expenditure on everybody else.
And if I increase the prices
of any other country's good,
that's going to raise expenditure
on the good produced by country I.
Okay. And
so we know that this system is
going to have a unique equilibrium
wage factor that's going to satisfy
that system of equations.
The equilibrium in
the model is unique.
Now when we're interested in this
question of economic dependence,
how much does my welfare depend
upon growth in other countries?
I'm now wanting to think about
a general ethereum experiment.
I'm going to say if I'm going to
look at the system of equations and
I want to know the answer to
the following question.
If China's productivity increases,
so if Z goes up in China, what is
the impact of that on my wage?
Firstly on my nominal income.
And then what is that?
The effect of that on my welfare.
So how would we
typically do that in trade?
Well the standard approach
to solving for
a counterfactual like that.
So what happens if there's a shock
to China's productivity?
What does the model imply will be
the effect on wages and
real income?
Well the state of the art way of
doing that will be the so
called exact algebra.
Counterfactuals introduced by
Decoleton and Cortan are widely
used in trade now.
So for those of you who
don't do trade as much.
This may be a little bit less
familiar, but I think it's
also diffusing a macro as well.
What's so beautiful about this
way of doing counterfactuals?
Well, let's think about
an initial equilibrium and
a counterfactual equilibrium.
And let's denote
a variable in the counterfactual
equilibrium by a prime.
So X prime will be the value of X
in the counterfactual equilibrium.
And let's denote the value
of a variable in the initial
equilibrium by X, where typically
we see the initial equilibrium in
the data, it's observed.
And then let's define
a relative change of a variable
between the counterfactual and
the initial equilibrium by a hat.
So X hat is just equal to X prime
divided by x.
It's just the relative change
in the variable between
the counterfactual and
the initial equilibrium.
Why is that notation useful?
Well, if I go to my general
equilibrium system of equations and
imagine that system of equations at
the top of the page, but for
the counterfactual equilibrium, so
write a prime for
the endogenous wages on all
the endogenous wages and I know all
the perimeters of the modeling
potentially could change as well.
So prime on every variable
in that system.
And now let's rewrite that
system of equations all written
with primes on every variable
in the following form down here.
Look on the left hand side of the
equation I've got W prime L prime.
Well, just as an accounting
identity, I can rewrite that as w
times l times w hat L hat.
Why? Because W hat L hat is
the primes divided by no prime.
So I've got primes divided by no
prime, the no prime cancel and
I'm back with the prime.
And so I'm just taking
the counterfactual system of
equations written with the prime,
but I'm just rewriting it
in an equivalent form as
an accounting identity so that I
can rewrite the entire system
simply using initial values of
variables that I see in the data.
That's the key advantage of this,
is I see the initial equilibrium
and the relative values which
are the things I don't see things.
I want to solve for
relative changes in
the counterfactual equilibrium.
And then I've done exactly the same
thing on the right hand side and
I've done exactly the same thing in
the expenditure shares as well.
And when I do that, what's nice is
when I write the hat terms and
then I've got the terms
without the hats, I can Replace
those terms without the hats by
the observed expenditure shares.
Okay.
And so what's so beautiful about
this is I want to solve for
the impact of a productivity shock,
a change in Z
on the endogenous wages.
And by rewriting that system of
equations in the counterfactual
equilibrium in the way,
I can answer that question
without knowing anything about
the initial level of productivity
in any country around the world and
without knowing anything
about the value of trade costs,
bilateral trade costs between
each country around the world.
Why?
Because they're absorbed in
the observed expenditure shares.
They're capturing the trade costs
and also embodied productivities.
And then the observed wages also
affected by productivity is also
embodied in those observed wages.
And so essentially I'm eliminating
the things I don't observe and
replacing them with endogenous
variables I observe
in that initial equilibrium.
And then if I hold the endowment
constant, then l hat will be one
and I'm holding TRACOS constant.
So the only thing I'm changing is
productivity here.
Well, now I've got a system of
equations where I'm feeding in
an assumed change in productivity.
So that's something I know.
Everything else is observed and
I can just solve that system for
the w hat,
the unobserved changes in wages.
And so I'm able to solve for
a counterfactual just using
observed values of variables
in initial equilibrium.
Okay, so very, very powerful,
widely used in trade because it
avoids having to estimate all those
unobserved fundamentals.
Yeah.
>> Speaker 2: So the interpretation
of that is dependent on
the numerator that you choose,
which is like the word gdp.
So let's say like if you say
wage goes up, you are actually
saying wage as a percentage of gdp.
GDP is going up, but we
know nothing about the world gdp.
How the productivity shock is
changing.
>> Speaker 1: It's a great
question. So you're ahead of me.
Something I was going to say next
and you'll see that's going to be
coming up on a later slide.
So let's look at that question.
Let's look at the system
of equations.
What do we notice
about the system of equations?
So I'm going to restate
your question in a different way.
This system of equations is
homogenous of degree 0
in the relative changes in wages.
In other words, imagine I multiply
both sides of the equation, I
multiply all the relative wages by
some multiplicative scalar lambda.
Okay, well, the lambdas are going
to cancel from the numerator and
denominator.
The lambda is going to cancel over
here and over here and so
that system of equations is
homogenous to degree zero wages.
So absolutely, to recover
a particular value of wages,
I need to impose that numerator.
That's why I've imposed it earlier,
and I'll say more about
that in a second.
But the relative value of wages can
be uniquely determined from
the system of equations.
Why? Because we know the system has
a unique equilibrium.
So up to a normalization or
a choice in numerator, we can pin
down relative wages uniquely.
Yeah, that's a great question.
So if I wanted to ask my question,
how dependent is my welfare on
growth in each country?
I know exactly how to do it.
I can just feed in those assumed
changes in productivity in every
country, solve
that system of equations for wages.
And the top slide there, I've just
rewritten that system of equations
in a slightly different way.
And you'll see
in a second way I've done that.
So what have I done in particular,
I've taken these terms in W and
zi outside the summation because
they don't depend on n. And then
I've defined a new variable I've
called T. And what is tin here?
Tin is the share of country I's in.
Income that comes from market N. So
it's an income share instead of
an expenditure share.
It depends on the expenditure
shares income in market N
divided by income in exporter.
I've just defined that T there.
And then I've just taken the terms
in I outside the summation,
taking the power over to
the left hand side, and
then raised the whole thing to that
power on the right hand side.
And I've just rewritten it in
an equivalent form and you'll see
why I've done that in a second.
And then I've now also
written the change in welfare.
And what's that change in welfare?
Well, that's just the change in
wages relative to the change in
the cost of living.
And again I can rewrite that using
my hat algebra in terms of relative
changes in the endogenous wages,
the exogenous productivity I'm
feeding in, and
then the initial expenditure shares
in the initial equilibrium.
Okay, and so one feature again
related to that question.
The change in welfare is not going
to depend on that choice
of numerator, right?
Because we mentioned earlier we can
only pin down wages
up to some multiplicative scalar.
But the multiplicative scalar here
will net out between the numerator
and the denominator in welfare.
And so welfare is
actually uniquely pinned down
regardless of the numerator.
So now I'm kind of in business.
I know how to solve for
how does growth in a country such
as China, how does that affect my
normal income up
to my choice of numeraire?
And how does it affect my welfare?
What's the limitation about this
exact hat approach?
Well, when I'm thinking about how
dependent is my growth on China and
I want to solve this system of
equations, I have to
assume something about how big
the productivity shock is in China.
I have to assume a size for z hat
the change in productivity shock.
And I have to do this
counterfactual N times for every
single country around the world.
I have to say what happens if
China's productivity increases
Sold for the ge?
Then, then say what happens if
productivity Malaysia increases?
Do the ge.
But I can do that and
I can sort of calculate a whole set
of arc elasticities.
What's the log change in my welfare
divided by
the log change in productivity
from a productivity shock.
And that's going to tell me
how sensitive is my welfare
to a productivity shock
in each country around the world.
So I do that n times my N countries
and I'm going to be able to
populate a matrix.
How dependent is the welfare of
every country in the world.
So those are the rows of the matrix
and then the columns of the matrix
are shocking productivity in each
country around the world.
So I shock China once and
I get a prediction for
the change in the welfare of every
country around the world.
That's a vector.
And then I shock
every other country.
I'm adding in an extra vector until
I populate the whole matrix.
Okay, limitation is I have to
assume the size of a shock and
I'm effectively computing
an arc elasticity,
a sensitivity of welfare for
an assumed size of a shock.
Yeah.
>> Speaker 2: So would you
also worry about something like
the cross elasticity is not being
identical?
So like with Armington trademark
you have all the cross elasticities
are identical.
So if you worry about something
like China is very substitutable
with some countries but
not other countries.
>> Speaker 1: Yep. So
great question.
So let's
restart that question another way.
So it's related to what I said
earlier about the independence of
relative alternatives.
So the independence
of relative alternatives says that
the relative expenditure shares for
two countries.
So US expenditure share on India
and China just depends on their
relative prices.
Doesn't depend upon the price of
Afghanistan or
any other third country.
Closely related implication of that
is that the CS demand system
imposes very strong
cross substitution restrictions.
When China's price goes up,
what does the CES demand system say
happens to all other countries?
Well, it's going to depend upon the
elasticity parameter, the theta,
the trade elasticity here.
And it's going to depend on the
initial index penetra shares and
everything is going to be symmetric
depending upon the trade elasticity
and the initial expenditure shares.
And that is for
sure a limitation of this cosmic
elasticity class of trade models.
And you'll see the exact cross
substitution effects.
I'm going to delve into them in
a little bit more detail in
a couple of slides.
Yeah, great question.
So there is some
work trying to relax this constant
elasticity assumption.
So for example, Costas Akalakis and
Sharat Ganapati have a paper where
they try to estimate this demand
system non parametrically using
the techniques of Berry and Hale.
From the IO literature.
I have a kind of a theoretical
paper with Mark Melitz where we
kind of make that point that if
the train elasticity is variable,
it matters for the impact of shocks
such as trade costs on welfare.
And it can substantially change the
welfare predictions of these models
if you have a variable elasticity
rather than a constant elasticity.
Yeah, great question.
Cool. So that would be the standard
way of doing this in kind of trade
using exact algebra.
One of the things we've been sort
of popularizing some of our work is
that there's also another way of
thinking about these questions,
which is that to do something
that's very common in macro and
international macro and
that's to linearize the general
equilibrium system of the model.
Okay, so what are we going to do?
Well, we're going to start with
that exact same income equation
here at the top of the page and
we're just going to
totally differentiate that system.
And that's exactly what we've got
at the top of this slide here.
I've just totally differentiated
that system of equations.
So taking the total derivative DW
and then dividing through by W,
writing everything as dw,
which is d log W and just doing
a standard linearization that we
do in macro all of the time.
And then what have I got on the
right hand side of the equation?
Well, you'll see that I've actually
got something that looks remarkably
similar to the exact algebra.
I've got the things that are
endogenous of the changes in wages.
So now I've got D logs instead of W
hats.
The exogenous thing I'm feeding in
are the DZs.
They're the productivity shocks
there in the right hand side.
And then I've got my single
parameter, the trade elasticity.
And then I've got the initial
expenditure shares, the little S's
and the variable I defined, the
income share, little T. Remember,
little T is the share of income
that country I gets from market.
>> Speaker 2: N.
>> Speaker 1: If you go back to
this slide, you actually see that
when I rewrote the nonlinear system
in this way,
it's actually remarkably similar
to the linearized model.
It's just here I have a log of
a weighted mean where the weights
are the income shares,
whereas in the linearized model I
have a weighted mean of the logs,
the change in the logs.
Right. And so these things
are very kind of closely related to
one another because this
is a constant elasticity system.
So just totally differentiated that
income equals expenditure equation.
And then obviously I can
do the same for welfare.
Take the total derivative,
it's just the change in wages.
And then it's going to be
the expenditure share weighted
average of the change in wages and
the change in productivities.
That's the usual first order
approximation for the change in
the cost of living with respect to
a change in the price of the good.
And again, very similar to the
expression in the nonlinear model,
except I've got logs of a weighted
sum versus a weighted sum of logs.
So what's nice about
this linearization is it actually
gives you a lot of intuition for
what's going on in this general
equilibrium system
when there is something like
productivity growth in China.
And we can see that if we sort of
relabel some of these terms.
So what I've done now is
I've rewritten that system
of equations in matrix form, okay?
So I'm totally differentiating
the whole system.
So on the left hand side I've got
the change in the wage
of every individual country.
I'm going to stack them
in a vector of the D log changes so
the bold font here is a vector and
then I'm going to stack everything
on the right hand side So
I can write those sums in terms of
the T's times the D log ws.
I can write that as the matrix of
income shares times the vector of
changes in wages.
That's just rewriting the sum in
matrix form.
And then I can rewrite those
terms in the product.
Of the t's and
the s's, that summation,
I can again write it in a matrix
form where I've got a scalar theta
and then I've got another matrix M
times d log w minus d log c,
where again those are both vectors.
And this matrix M related to
Oliver's question
is the cross substitution matrix.
So let's sort
of talk through that intuition.
What happens when
China becomes more productive?
Well, that's going to affect wages
in every country around the world.
So wages in each country around
the world are going to change in
general equilibrium and
that's going to affect my income.
On the left hand side, how much is
a change in wages in any market
going to affect my income?
Well, that depends upon what share
of my income I
get from that market.
So this first term here is
essentially a market size effect.
And when there's a change
in productivity,
there's a G effect on wages in
every country around the world.
That changes market size around the
world and that affects my income.
And then the second term here is
exactly this cross
substitution effect that Oliver
was thinking about.
When China becomes more productive,
what does that do in every market
around the world?
Well, in the German market,
Chinese goods are now cheaper.
And so I'm going to sell less of my
goods in the German market because
I now face a tougher competitor.
Chinese goods have become cheaper.
What does CES demand system say
determines that cross substitution?
It depends critically on
the expenditure shares and
the single constant elysisti theta.
Right.
And so as China gets some
productive more productive in
the German market, I lose some
expenditure in that market.
How much do I lose?
It depends on expenditure shares.
How much does that loss in
expenditure affect my income?
Well, it depends upon the income
share I get from the German market.
And that's why
the cross substitution here is
the product of the income share and
the expenditure share.
Okay, so it's just rewriting that
system of equation in matrix form
and in the linearized model you get
this kind of clear understanding of
why a country could be a friend or
an enemy in economic terms.
So when China becomes more
productive, that could
either increase or reduce my wage.
Why? Because it depends upon how
market size changes around the
world and the share of my income I
get from each of those markets.
And it depends upon these cross
substitution effects.
So my income could go down if I
compete heavily with China.
If I get a big share of my income
in markets where China accounts for
a large share of expenditure,
that's where I'm going to be
really hurt
by growing Chinese productivity.
Then again, I can stack the real
income exposure equation in matrix
form where I've got the vector of
changes in welfare, the vector of
changes in income and that vector
of changes in the cost of living.
What's the advantage of this
linearized model and
what's the disadvantage?
Well, the disadvantage is obviously
a first order approximation.
I'm linearizing.
And so for large changes the worry
might be we don't know how good
that approximation is going to be.
And I'll show you some evidence on
what that looks like,
the approximation error.
What's the advantage?
Well, the advantage is that we can
actually instead of having to do n
separate counterfactuals.
So what happens when I shot
productivity in China
to the welfare of every
country in the world.
Then I shot productivity in Ghana,
I shot productivity in
Brazil and so on.
And I have to do N counterfactuals
in the exact algebra approach here
I can recover that whole matrix
of exposure from a single matrix
inversion.
So in particular,
what am I going to do?
I'm just going to take all the
wages over to the left hand side of
this equation, I'm going to take
a matrix inverse and then I'm going
to be able to recover the whole
matrix of bilateral exposure from
a single matrix inversion problem.
Ok and this is where our choice of
numerator is going to be
important because obviously we can
only determine wages or
up to the numeraire.
So in order for that matrix to be
invertible, I'm going to have
to impose that choice of numeraire.
Why? Because the expenditure share
sum to one, so the rows and columns
of the matrix are not all going to
be linearly independent unless I
impose a choice of numerator.
So that's what we've done here.
We're just going to impose our
choice of numeraire.
So all I've done in the top line,
I'm just rearranging that
wage equation,
just dividing through by theta +1.
Then I'm just taking all
the terms and
wages over to the left hand side.
We can write that as the identity
matrix minus t minus theta m,
taking the terms in T and
theta m from the right hand side to
the left hand side.
I'm now going to define that cross
substitution matrix M as ts -I.
So that enables me to rewrite it
in the line below and then I've
just rewritten it a slightly more
parsimonious form there.
Then finally I need to in order for
this to be invertible.
So this here is not invertible
because the expenditure shares and
the income shares sum to one.
So in order for that
to obtain invertibility, I need to
impose my choice of numeraire.
Remember I said that
my choice is that the sum of
the q's is equal to 1.
Well, that means the sum of the q's
times d log w has to be equal to 0,
just taking the log
total derivatives in that choice of
numeraire.
And I can rewrite that sum of
the Q's times the D log wages
equals zero as just the product of
a matrix Q which has rows equal to
that income vector.
So it's just populated with rows
equal to the income vector
multiplied by d log w.
That's how I'm going to impose
my choice of numeraire.
So I'm just adding this term in on
the left hand side because under
my numerator
I know that term is equal to zero.
So it doesn't change
the left hand side at all.
And so now I can just invert that
equation and I'm going to recover
what we call the friends and
enemies matrix.
So W here
is that term I just derived theta
over theta plus 1i minus V inverse,
where V are those terms in T and
t times S from the previous slide.
And then
what is my welfare exposure?
Well, once I've inverted the model
and I've got the W matrix,
welfare exposure is just
the identity matrix minus
the matrix of expenditure shares
times the W matrix plus the matrix
of expenditure shares.
And so I could just do
a single matrix inversion.
Takes fractions of seconds on
a modern computer and
I get a whole matrix of
exposure for the whole world.
So that's particularly powerful if
you want to do a large number
of counterfactuals.
It also gives you
point elasticities because
I'm looking at small changes here.
So I'm getting exactly
how sensitive is my welfare to
changes in productivity in China,
I don't have to pick a size of
the productivity shock as I did
in the exact algebra, and
I no longer get an arc elasticity,
I get a point elasticity.
So that's kind of an alternative
way of thinking about constant
elasticity trade models just using
standard linearization techniques.
What are the insights you get?
Well, you understand the kind of
mechanisms, the market size effect,
the cross substitution effect, and
you get this ability to just invert
the model and get the full matrix
of welfare exposure to productivity
growth in every country around
the world as a single matrix
inversion, just to sort of flag.
Obviously I'm illustrating this
in the sort of
standard class of trade models
where we have a single sector model
with a constant trade elasticity.
This methodology
is actually much more general.
So we show in the paper
a very similar representation holds
in a multi industry model
without template output linkages
like Costner, Donaldson and
Camanja, for those of you familiar
with that paper, or
a multi sector Armington model.
Same representation holds.
Same representation holds also in
the Caliendo Paro paper I
mentioned earlier.
You can rewrite
everything in this matrix form.
The only thing that changes is you
have to change these expenditure
share matrices and income matrices
and cross substitution matrices.
Why? Because in a country industry
model, the US Competes with China
in the textiles market
in Germany, right?
So it's the country,
it's the market industry where
I'm competing, and the expenditure
shares and the income shares
could be different.
In different industries.
China could be a very strong
competitor in Germany in textiles
in the sense that accounts for
most of the market, but
it might be a weak competitor in
Germany in another sector.
>> Speaker 2: Yeah, but
this matrix is still
first order in some sense, right?
It only captures the direct effects
and not the fact that for instance,
if China productivity increases,
it increases productivity in Mexico
and that affects
the US So great question.
>> Speaker 1: So let's think
about that.
So you're absolutely
right that this matrix inversion
is first order.
So it only captures first order
effects, but it does capture
first order GE effects, so
it captures the full GE feedback
because essentially we're solving
this entire system of equations,
but just the first order terms.
So it does have some GE feedback.
So we're taking account
when China's productivity goes up,
wages in Germany might change and
that affects my wage as well.
So we've taken those into account,
but we're abstracting from
the second order and higher terms.
And as you pointed out,
we're treating the productivity of
every other country as fixed.
So we're not thinking
about knowledge spillovers or
endogenous technology.
But it does capture first order
G effects in this class of models.
Cool.
So in the multi industry model,
we have to think about competitions
in an industry and expenditure
shares and income shares may vary.
And then obviously when we have
input output linkages,
we have to take account of the fact
that if I'm using Chinese goods as
an input, higher productivity in
China might not be good for me
because it lowers my input prices.
So we need to take account of
the full value chain,
the full structure of the global
value chain.
But again, in the Caliento
para model,
which assumes like a Cobb Douglas
input output structure, we get
exactly the same representation.
We just have to construct the S,
T and M matrices in the right ways,
which what do they depend on?
Well, they depend upon observed
things like expenditure shares,
cost shares and
trade elasticity as before.
But also the Cobb Douglas shares in
the input output table are going to
matter in the construction of those
matrices.
Cool.
So let me sort of illustrate this
first application, show you what
we found very quickly and then talk
about how we can combine these
constant delicacy trade models,
use these linearization techniques,
but bring them together with an
international macro model where we
have both trade and capital flows.
So we're going to use some of the
comp trade database I mentioned.
We pull the cepigravity to get us
income, population and distance.
And then we are going to measure
political alignment using United
nations voting strategic rivalries
measured by political scientists.
And measures of formal alliances.
We're going to use a sort
of technique that's
pretty common in trade
to get measures of trade costs.
We're going to invert
the equilibrium conditions of
the model.
So we're going to recover
bilateral trade costs from what's
known as the head Reis index.
So that's noticing that we want
to find out tracost to feed in
the shocks into our model, but
we don't directly see them,
as I mentioned earlier.
But if we
observe bilateral exports, so
exports of importer N from exporter
I relative to importer N's
traded itself and then we also
observe the mirror flow of that
xint relative to I's traded itself.
So if you compute those ratios,
raise them to the power,
then on the right hand side
everything cancels.
All the exporter fixed effects
are differenced out and
all the price indices, terms or
the denominators cancel out again
because of the double differencing.
So it's a kind of
trick often used in trade.
If you take that double difference,
you eliminate the exporter
characteristics and you eliminate
the import characteristics and
the only thing you're left with
is the bilateral characteristics.
And if you're willing to believe
trade costs are symmetric and
you normalize your trade costs with
yourself to one, then you're going
to recover bilateral trade costs
between the two countries
up to that assumption of symmetric
trade costs.
So we're going to just use that to
get a sense as to what would be
empirically plausible set of trade
cost shocks to feed into the model.
And once we've got our trade costs,
we then back out productivities
again up to a normalization because
it's homogeneous of degree zero
from this income accounting
relationship.
To get to back out from the data
an empirical distribution of
productivity is to feed into model
of shocks.
And then related to questions
earlier about how good is
the approximation.
So we actually find for
productivity shocks,
the first order approximation is
in these models is extremely good.
So essentially here we're reporting
sort of Monte Carlo evidence
where we're going to feed into
the exact algebra
a set of productivity shocks.
And what productivity shocks are we
going to choose?
Well, we're going to choose
a weighted average of the empirical
change in productivity between
1970 and 2012 backed out from
our model inversion.
So that's a big number because it's
a productivity change
over more than 40 years.
So that's going to be the extreme
when we have a weight of one on
those empirical shocks.
And then the other extreme is we're
going to have a vector of ones.
So we're going to place a weight of
0 on the empirical productivity
shock and a weight of 1 on
the vector of ones, in which case
there are no shocks because
the relative change in productivity
z hat is equal to one for
every country around the world.
And then we're going to report
everything in between,
all the weights in between,
placing 1 on the empirical vector
of productivity shocks and
placing 0 on it and a weight of 1
on a vector of wireless.
And what do we find?
What we find for productivity
shocks on the vertical axis,
I'm reporting the correlation
between the predictions of our
linearization for log changes
in welfare and the predictions of
the exact algebra counterfactuals.
And you can see for
productivity shocks, they're almost
exactly the same correlation,
very close to 1.
For tracoff shocks,
the correlation is less good.
And as we place a weight of one on
the empirical changes in trade
costs, we get down to some
lower correlations.
That makes a lot of sense, because
let's think about what the second
order terms are that we're emitting
from this linearization.
Well, they're terms in the changes
in the shares times the changes in
the productivity shock.
Those are the second order terms.
If you think about a shift in
productivity, it's an exporter
characteristic that's common across
all importers trading with that.
So it's something that sort of
differences out across some of your
bilateral pairs.
And so productivity shocks don't
lead to as big changes in shares
as bilateral trade costs,
because bilateral trade costs
are bilateral, they only affect one
partner and hence lead to
a larger adjustment in shares.
And so that's sort of one intuition
for why the first order
approximation is better for
productivity shocks than it is for
trade cost shocks.
But even for
pretty big trade cost shocks,
the approximation is pretty good.
So this is a measure of
global welfare exposure.
So we've got our matrix now of how
exposed is each country around
the world to productivity growth in
any other country?
And this left panel here is showing
average welfare exposure over time.
The right panel is
showing the standard deviation of
welfare exposure over time.
And so we're computing this in
every year based on
the observed expenditure share and
income share matrices in that year.
And you can see a story of rising
globalization, that over time
countries are now more exposed to
one another as productivity growth,
consistent with there being
globalization during this period.
And we also find that welfare
exposure becomes more dispersed,
again, potentially consistent with
growing globalization.
And now there's sort of
more heterogeneity
in that welfare exposure between
pairs of countries.
We validate our welfare exposure
measure by sort of showing that if
you regress it on measures of
countries signing free trade
agreements, you'd expect welfare
exposures to go up when you sign
a free trade agreement because it
lowers trade barriers between you.
And so we report events, study
evidence in the paper showing that
we find that measure of welfare
exposure responds very strongly
to this completely separate measure
of trade agreements that we didn't
use at all.
>> Speaker 2: And. Anywhere in how
we computed welfare exposure,
just as a kind of validation effect
that we sort of really think we're
capturing welfare exposure.
And then because we've got this
matrix of welfare exposure,
we can sort of use measures from
the networks literature
that think about characteristics
of that network.
So what are the measures we're
going to use here where we're going
to use measures of authority score
in hub school, which is sort of
a generalizations of notions of
eigenvector centrality to the case
when you have a directed network.
So the authority score is going to
capture how important is a country
as a source of real income shocks
for other countries.
And the hub score is going to
capture how important is a country,
how sensitive is a country to
productivity shocks in
other countries.
So an authority means I have a big
effect on other countries.
Hub means I'm very affected by
other countries.
I'm very sensitive to
other countries.
Okay?
And so those are those measures.
And so once you give me the matrix
of welfare exposure, I can compute
those hub and authority scores for
each nation around the world.
And again, we see a sort of
intuitive pattern here.
I plotted those measure,
the measure of authority score.
How important is a country as
a source of shocks to others,
to the welfare of others?
And unsurprisingly you find
Japan becomes much more important
during its period of rapid growth
in the 1970s and 1980s, and
China becomes much more important
as a source of shocks to others
during the 1990s and 2000.
And those changes in authority
scores are actually much bigger
than the changes in relative gdp.
So again, there's some
extra insight from actually using
the structure of the model and
computing welfare exposure
in the model consistent way.
I want to make sure I have
time to talk about the kind of
international capital side.
So I'm not going to spend a lot of
time time on the sort of evidence
in the paper, but I'll just kind of
show you one brief glimpse of it
and then you can sort of delve into
the paper in further detail
if you want to look at the sort of
IV results and look through at each
of the different IV specifications.
So in the panel here, this is just
sort of showing you some,
some simple correlations.
In the top panel
we've got welfare exposure
to productivity growth by country.
And on the left we've got the
values in 1980, and in the right
we've got the values in 2010.
So 1980 is just after China's
domestic liberalization in 1978.
And then 2010 is at the end of our
Sample period.
And you can see this
dramatic increase in exposure,
welfare exposure, as China grows,
particularly in East Asia.
And this is from the kalia no PARO
input output structure
version of the model.
So modeling
all of the input output linkages.
So in factory Asia, we see growing
welfare exposure to China, and
we also see
a large increase in welfare
exposure in sub Saharan Africa,
also to some degree in Oceania.
And then in the bottom panel,
we plot voting similarity to China
in the United Nations General
assembly in 1980 and 2010.
You can do that in different ways.
It doesn't particularly matter
which way you do it.
This is the sort of
most sophisticated measure
we have available.
And you see this sort of a striking
similarity in this increase
in voting patterns with
the increase in welfare exposure.
And that's clearly
only a correlation.
And in the paper we developed those
two different IV strategies I
mentioned to try to kind of
make the argument this is actually
kind of a causal relationship.
Okay, so that's my first of the two
projects I wanted to talk about,
sort of illustrate how we can use
these constant delicacy trade
models, use them as a way of
computing welfare exposure,
income exposure, and linearize
these models to be able to compute
those measures of general
equilibrium linkages, that network
of linkages in the world economy as
part of a single matrix inversion.
What I want to do in the rest of
the talk is now connect with some
of the work on the Global Capital
Allocation project and connect with
some of Antonio and Matteo's
lectures as part of this week.
And now show how we can combine
this trade model with a standard
macro model and try to develop
a framework where we have
linkages between countries in both
goods markets and capital markets.
Okay, so
how are we going to do that?
Well, we're going to take
essentially the standard
closed economy neoclassical model
of growth, the Ramsey model,
which is a benchmark for
thinking about cross country income
dynamics in the macro literature.
And we're going to blend it exactly
with that constant elasticity trade
model which we know is a benchmark
for thinking about trade
linkages between countries.
And we want to think about how this
trade and capital model interact
with one another.
How does trade matter for growth?
How does growth matter for
the impact of trade shocks?
And of course, one big limitation
of the closed economy neoclassical
Ramsey model is that each country
is essentially in financial and
trade autarky.
There's no reason for trade,
there's a single good.
There's no borrowing or lending.
In the basic closed economy
Ramsey model, completely financial
autarky, and countries have no
reason to trade so what we're also
going to do is we're going to
open up that model and allow for
international capital holdings in
order to try to be able to connect
the model to, to the data
that we observe from the GCAP
on global capital holdings.
And we're going to ask the question
how do the linkages in trade
markets and the linkages in capital
markets through those bilateral
holdings change our understanding
of the growth process and
of the impact of trade shocks.
So what we're going to try to do,
we're going to try to
develop a framework where we have
intra temporal goods trade.
So just like the model we
discussed, countries are going to
be trading with one another
at a point in time.
We're going to have intratemporal
capital holdings.
So we're going to countries
are going to have bilateral
holdings of capital
like we see in the GCAT data.
And we're also going to have
intertemporal consumption saving
choices because obviously,
just like in the Ramsey model,
countries have to be accumulating,
making decisions about saving
an investment over time.
And so we're going to have
endogenous current accounts and
sort of be
modeling that explicitly.
Okay, so what are we going
to get out of this framework?
Well, we're going to show that
the resulting framework is going to
be able to match a number of key
features of the observed data.
So we're going to make sense of
the fact why we see a gravity
equation for trading goods, but
then also maybe less well known,
but it's also another
good description of the data
where we see a gravity equation for
capital holdings as well.
We're going to have a determinant
predictions for gross and
net capital holdings.
So the model is going to explain
why gross holdings are much bigger
than net capital holdings.
As Antonio was discussing at the
beginning this morning, the model
is also going to give us a way of
thinking about the Lucas puzzle.
Why does relatively little capital
flow to capital scarce countries?
Which is puzzling in terms of
the standard Ramsey model,
at least standard open economy
versions of that would imply that
all the capital
should flow between countries to
equalize rates of returns.
And that's not what we
seem to see in the data.
And the model is also
going to explain why we see home
bias in trade and
capital flows, why both trade and
international capital holdings
are disproportionately concentrated
domestically relative to what you'd
expect based on country size.
And then finally,
the model will also give us a nice
way of thinking about the so
called Felstein Herioca puzzle.
Why domestic and saving and
domestic investment are very highly
correlated with one another.
Okay, we'll show how we can sort of
generalize those exact algebra
techniques I was discussing in the
first lecture, how they'll still
work even in this dynamic model
where we've got dynamic capital
accumulation and open economy
portfolios of capital holdings.
And we'll also show how we
can use similar
techniques to linearize the model.
And now once we linearize it,
we don't just characterize the G at
a point in time.
We can actually solve in closed
form for the entire transition
path, closed form solution for
the entire transition path to
the economy over time.
Because we've now got this
framework that has both
bilateral trade and
bilateral capital holdings.
As I said, we can think about how
trade influences growth,
how growth influences trade.
We can ask questions like what
will happen if China and
the United States decouple
not only in goods markets, but
also in capital markets.
How does the presence of capital
market linkages affect the impact
of a decoupling in goods markets?
And again, we're obviously building
on a vast literature here,
including importantly the work by
Matteo and
colleagues here at the gcat.
So let me give you the quick model
setup and then we'll
dive into a little more detail,
into the equations of the model.
And then I'll try to give
you the kind of key punchlines that
we get from bringing these
frameworks together.
So we're going to think of
a country of economy of consisting
of many countries around the world.
Just like in the trade
model we saw,
time is going to be discrete and
indexed by T. Each country is going
to supply a differentiated good.
It's produced using labor and
capital under constant returns
to scale.
So again, we're going to be in
an Armington model.
But as I said earlier, everything
we do here in the Armington model
will hold in any constant
elasticity trade model.
So pick your favorite constant
elasticity trade model or
all the results will go through.
Only difference is now we've got
capital as an additional factor.
As well. As labor markets are
competitive, goods can be traded
subject to bilateral trade costs.
There's a representative agent
in each country who's endowed with
a measure of labor, just like in
the trade model we saw.
But now here's going to
be the different component.
At the beginning of period T,
our representative agent in each
country is going to inherit some
initial stock of wealth A and
she's now going to decide how much
to save and how much to consume.
So she can make choices about the
accumulation of wealth over time.
And she's also
going to make decisions as to
where to allocate her wealth.
And so in particular, she can
choose to allocate her wealth to
every country around the world.
So we're opening up the Ramsey
model, allowing the representative
Asia to hold wealth in any country
around the world, subject
to capital market frictions and
subject to some idiosyncratic
shocks that I'm going to talk about
more in a moment.
At the beginning of period T,
she's going to choose her wealth
allocation across countries and
make her consumption
saving choices.
And then at the beginning
of period T +1, investment
returns will be realized.
Depreciation will occur and
wealth will again be allocated
across countries.
Just flag one big simplification
we're making relative to some work
in international macro and
international finance.
The model we develop here is going
to have no aggregate uncertainty.
So we're going to be solving
the model under perfect foresight.
So we're not going to speak to
the recent literature on
international risk diversification.
But nonetheless,
even though we're abstracting from
aggregate uncertainty and
international risk diversification,
we're going to sort of show that we
can explain many of the observed
features of capital holdings that
I talked about earlier.
And for those of you interested in
aggregate uncertainty,
we're doing some new work where
we're actually trying
to model aggregate uncertainty
in these types of models.
And there's a draft,
initial draft of our paper
on that topic on our web pages.
Cool. But now let's dive into
a little bit more details.
So the consumption saving choice,
we're just going to make it
plain vanilla.
We're going to take the standard
consumption saving model for macro.
So we're going to have
representative consumer constant
relative risk aversion preferences.
So beta is the discount rate
size and
temporal associate substitution.
And then we're going to have
consumer maximizing her internal
utility subject to her period
by period budget constraint.
So the value of her consumption
plus the value of her wealth next
period it's going to have to equal
her labor income plus her income
from existing stock of capital,
net of depreciation.
And the only thing that's non
standard in that period by period
budget constraint is
stock of wealth.
An is being held in every
host country I and I'm going to sum
up across those host countries and
notice the way I've written it,
I've taken the rate of return on
those holdings, which is V.
I've taken that outside of the sum
because in equilibrium it's going
to be the same
across all of the host countries.
That's why I'm able to do that and
I'll prove that to you in a second.
I can actually then just rewrite
that period by period budget
constraint in exactly the standard
macro form where calligraphic R
here is the real gross return
to investment.
So we know how to
solve that problem.
What is the solution?
Well, with constant
relative risk aversion preferences,
consumption is going to be a linear
function of current period wealth,
as for example in Angeletos 2007,
where that linear function var
sigma here is going to be
determined recursively between each
pair of periods as down here.
So in the special case of
logarithmic utility var sigma here
would just be one minus beta and
you'd have a constant
rate of consumption and a constant
rate of saving out of wealth.
If preferences were log, but more
generally with CRA preferences it's
a linear function, but that linear
term is not necessarily constant.
Cool. So that's standard.
What about the model of
capital holdings?
Well, this is now going to
be different.
And this is where we're actually
going to be bringing some
ideas from trade
into international macro.
So how are we going to think about
that capital allocation decision?
Well, I'm going to think about
our representative agent as having
a continuous measure of
units of wealth.
And she's going to choose where to
allocate each
unit in that continuous measure.
And for each of those units,
she's going to get
a vector of productivity shocks for
how productive it is
to invest that unit
in each country around the world.
And we're going to denote those by
fee nit.
So she wakes up, she's got this
continuous measure of wealth.
She thinks for every unit,
where shall I invest this?
She looks around the world and
she gets an idea for a productive
investment in every country.
Some of those ideas
are going to be better than others.
They're going to have a higher
productivity draw,
higher, higher fee.
And what is she going to do?
Well, she's obviously going to
allocate each unit of her wealth
to the country that offers
the highest rate of return.
So what is that rate of return?
Well, that's going to depend upon
the rental rate per effective
unit of capital in host country I.
It's going to depend
upon her productivity draw for
that host country I.
So fee nit
how good her idea was for
that country I, or the number of
effective units of capital she had.
Once we adjust for
the quality of the idea,
then in addition to the model,
we're also going to allow some
capital management costs.
So capa nit,
they're going to capture capital
market frictions where it might be
harder to manage capital abroad
than it is to manage capital at
home because of additional
information search matching costs.
So what are we going to assume
about these idiosyncratic shocks?
Well, for
those of you coming from the trade
side, you probably guessed already.
We're going to assume extreme value
distribution for
those idiosyncratic shocks.
So phi here is going to be drawn
from a fresh
a distribution up here.
Epsilon is going to regulate the
dispersion of those idiosyncratic
shocks to the quality of ideas.
And eta it is going to
be a scale parameter which will
determine on average, how good
are the quality of ideas for
a particular host country I?
So for example, US Assets might be
particularly good.
So the US has
got a high value of eta.
It's got a high draw for
the quality of ideas
that you draw from.
So what is the advantage of making
that extreme value assumption for
those idiosyncratic shocks?
Well, it's going to give us
two convenient properties
that keep the model tractable and
help us connect with the data.
First thing again
from trade you're all going to be
familiar with is it's going to give
us a gravity equation for
bilateral capital holdings.
So B and it is going to
be the portfolio share.
What share of the wealth
does the representative agent in
country N hold in host country I?
Well, that's just going to
depend upon relative rental rates,
relative value of that parameter
for the quality of ideas in host
country I and
bilateral capital market frictions.
But just like we saw in the trade
gravity equation, bilateral capital
holdings between N and I don't just
depend upon bilateral frictions,
but also multilateral frictions.
The value of the frictions with all
other possible host countries where
I could hold my capital.
So the model is going to deliver
gravity for capital holdings, which
I think I've got a slide on that
later, is a very good approximation
to the data on capital holdings.
If you take the GCAT data
which we're using, or any data on
capital holdings has that property,
it's a very strong
property of the capital data.
What's the second
convenient property?
Well, another property of this
fresh, a extreme value distribution
is that the expected return.
And because these idiosyncratic
shocks are idiosyncratic,
they're going to integrate out.
So the expected return will equal
the realized return.
Expected return conditional on
investing in a country
is going to be the same across all
host countries in equilibrium and
in fact will equal.
We have this nice closed
form solution for it down here.
So the return on my investment
if I'm in country N,
if I'm the investor in country N
is going to be the same across all
host countries.
I so different host countries can
have different rental rates and
they're going to face upward
sloping supply functions for
capital as we see in the gravity
equation here.
If I want to attract
a bigger portfolio share
from any investor country, I have
to offer a higher rental rate.
So I've got an upward sloping
supply function for capital.
So some countries can have higher
rental rates than others, but
the average return conditional on
investing in a country has to be
the same across all countries.
How is that possible?
Well, if a country has a high
rental rate, it's going to attract
investments with low realizations,
these idiosyncratic shocks.
And so there's
a composition effect.
It's going to attract
investments with worse ideas and
with a fresh a extreme value
distribution, that composition
effect exactly offsets the impact
of the higher rate of return or
the lower capital market frictions.
And that's a convenient property
because it means there's just a
single rate of return in the macro
consumption saving decision.
And that's what I used earlier
where I took that rate of return
outside the summation.
So those two features of the model
are going to mean that it stays
extremely trackable,
it's going to match the data and
gives us a tractable way of opening
up the Ramsey model and
bringing trade in as well.
Okay, what's the limitation?
Hang on one second.
I'll take question.
What's the limitation?
Well, as I mentioned,
no aggregate uncertainty here.
Okay, so we're going to be able to
match the capital data, but
we're not going to be able to say
things about changes in aggregate
uncertainty and
risk diversification.
Just make
a couple of points about that.
You actually can derive this
gravity equation of
capital flows in a variety of ways.
And in fact, there are some
models of international
risk diversification which would
also give you a gravity equation
that takes exactly the same form.
And so this gravity prediction,
just like in trade,
we have some isomorphisms.
If you're focused only on
the gravity equation,
there are also some isomorphisms.
You can derive it from this model
of investments we develop here.
You can derive it from
international risk diversification
models like yoga.
And there's several other possible
micro foundations, but in general
those models would imply something
else for the other equilibrium
conditions of the model.
So what's nice about this micro
foundation is it's going to enable
us to hit the penworld tables data,
the national accounts data.
It's going to connect directly with
physical capital data.
And the rest of the model is going
to stay very tractable and
we can use it to think about
the interaction between trade and
growth, which would be much more
difficult in a model of
international risk diversification.
And then let me take a question.
So here the state variable is
the total wealth.
So capital is not
accumulated within each country
across the time.
Right.
So great question.
So the state variable here in
the system is going to be
the measure of wealth in every
investor country.
So ant that vector will be the
state variable, vector of wealth.
And then as you pointed out,
each country there's also a stock
of capital in each country, but
that's not the same as wealth
because I can own some of
the capital in another country,
they can own some of my capital.
And so when we solve the model,
the state variable will be
the stock of wealth.
And we show
in the linearized model, the stock
of capital is just a linear
function of the stock of wealth.
So once you solve for the stock of
wealth, you can recover the stock
of capital and all the other.
Good question.
Cool. How about
the trade side of the model?
Well, this is going to be
super familiar because it can look
exactly the same
as the model we did in the first
part of the lecture.
So we've got Armington preferences
across countries with the constant
trade elasticity standard trade
gravity equation that we discussed
in the first part.
Only difference here is that
goods are produced with
labor and capital.
So we've got the wage
to the power of the labor share.
So we're going to assume
the Cobb Douglas technology
rental rate on capital to the power
of the one, minus the labor share.
And then again, ZIT is our measure
of productivity in country I.
One thing we have to be careful of
in the general liquor equations,
we have to do all
the accounting, right?
And so in particular, payments to
capital at the point of production.
So the rental rate times
the capital stock, which, which of
the Cobb Douglas technology is just
a multiple of payments to labor.
It's a property of
a Cobb Douglas technology.
So payments to capital at the point
of production,
they're going to have to equal
the income received by everybody
who owns capital that's used in
production in country I.
So income payments to capital
used in country I has to equal
the sum across investor countries
of the amount they're investing in
country I multiplied by their
expected return,
which as we mentioned earlier, is
common across all those countries.
It differs across
investor countries.
Okay. When we do that calculation,
one thing we need to take
account of is that the productivity
of capital is going to depend upon
those efficiency draws.
It's going to depend upon the
average efficiency draw conditional
on investing in a country.
And another nice feature of
the Fresh air extreme value
distribution is that we have
a closed form solution for
what is the average productivity of
capital conditional on investing
in a country?
It's just the constant velocity
function of the share of
my portfolio I invest.
There's.
So in some ways this model is
actually reminiscent of Keynes
idea of a diminishing marginal
efficiency of investment schedule.
If I invest more of my portfolio in
a country, I'm moving
down to worse and worse ideas and
there's lower and lower
productivity of those investments.
And this is the sort of micro
foundation of this,
of that idea using
an extreme value distribution.
Okay.
We just need to make sure we take
account of those average
productivities when we're measuring
the capital employed in production.
Cool.
So then how about
the equilibrium of this model?
How can we characterize it using
some techniques related to those we
discussed in the first part of
the lecture.
Well, what's the steady state
equilibrium going to look
like in this model?
Well, that's going to be
characterized by
time invariant fundamentals.
What are the fundamentals
in this model?
Well, that's the labor endowment in
each country productivity and the
quality of the capital environment.
Eta was that scale
parameter determining
the average quality of ideas.
Then also the matrix of bilateral
trade costs and the matrix of
capital market friction.
Those are going to be
the fundamentals in the model.
So those are going to be constant,
then the steady state the state
variables are going to be
the wealth stock in every country,
so a star n. So in steady state,
we'll have a constant vector of
state variables in each country
around the world.
And then all the other endogenous
variables in the model will be
constant, like wages, rental rates,
expenditure shares, average return
on capital, and portfolio shares.
In steady state, the gross return
to capital is actually the same
across all countries.
And that linear
var sigma term in the consumption
rule actually turns out to be equal
to 1 minus beta in steady state.
So with log intertemporal utility,
it's always equal to 1 minus beta.
With CRRA it's equal to
1 minus beta in steady state.
And that means that
in steady state,
the real return to investment
in terms of the consumption good.
Because just like in macro models,
there's a single consumption good
here I either consume it or.
Or invest it and create capital and
create wealth.
And so the price index is
the cost of a unit of wealth.
And that will be equalized across
countries as well in real terms
in steady state.
So how can we characterize
the equilibrium in the model?
Well, in the paper we show
you can use dynamic exact algebra
techniques, sort of pioneered by
Lorenzo Caliendo at Yale.
So he developed those techniques in
a model of dynamic
discrete migration.
Here we have a model of trading
capital holdings between countries.
So we don't have any migration, but
we have dynamics in capital.
And we show that you can generalize
those dynamic exact techniques.
And if you give me the initial
values of the endogenous variables,
and the economy is somewhere on
a transition path to steady state.
Doesn't have to be in steady state.
Can be anywhere on the transition
path to some unobserved steady
state with constant fundamentals.
As long as I see the initial values
of the endogenous variables,
in particular, the initial
expenditure shares for trade and
portfolio shares for international
capital holdings, and I see two
periods of wealth, so I actually
need two initial periods of wealth,
then I can solve for the transition
path in the absence of any further
changes in fundamentals.
And I can solve for
the transition path for
any counterfactual convergence
sequence of future fundamentals.
Okay, so we can use dynamic exact
algebra techniques and solve for
the transition path in
the nonlinear model, but
that's just a numerical algorithm.
Something else we can do
is actually linearize the model and
then characterize that transition
path in closed form.
And so I just want to
kind of advertise that to you and
why I think these sort
of techniques are exciting and
could be used more widely in
international macro and trade.
So we're going to think about
again, as I said, we observe
the economy at some initial time.
It's somewhere on a convergence
path to some unobserved
steady state that would arise
if there were no further
changes in fundamentals.
We're going to use a tilde above
a variable log deviation from this
initial steady state.
And then we're just going
to do our standard macro
total differentiation around that
initial unobserved steady state.
And what is that going to give us?
Well, just like in the trade model,
we're going to get a big system of
linear equations.
In the trade model, it was a pretty
small system of linear equations.
We just had the N equations for
each country for wages here.
Now we've got this.
When we differentiate all the
equivalent conditions, we've got a
larger system of linear equations.
But if you play with that system
Enough and you just substitute one
equation into the other.
You can actually reduce it down to
a second order difference equation
in the state variables.
So second order of difference
equation in wealth.
And so you can use all of
the techniques you're familiar with
from the dynamic stochastic general
equilibrium literature in macro,
you can solve that system of
second order difference equations.
You can either use Blanchard Kahn,
you can use Chris Simms method, you
can use the method of undetermined
coefficients, we use the method of
undetermined coefficients.
And so in the linearized model you
can actually get a closed form
solution for that transition
path of the state variables.
What does it look like?
Well, it takes the following form.
The vector of state variables at
time T is some function of the.
Sorry to back up a little bit.
When you solve that system of
differential equations,
difference equations, you obviously
have to make an assumption about
what's happening to fundamentals
when you solve that system.
So one thing you can assume is no
further changes in fundamentals and
then you can solve that system to
the unobserved steady state.
Other assumption you can make, and
it's going to be the one I'm
illustrating here is you can
imagine we see our economy
somewhere on a convergence path to
steady state.
And then we're interested what
would happen if there's a trade
cost shock or what would happen if
there's a productivity shock.
And we take a one time
unanticipated shock to fundamentals
and then we solve for
the evolution of the entire
transition path given that one time
permanent change to fundamentals.
And so I'll show you that solution.
Here in the appendix of the paper
we provide more general solutions.
You can solve it again for
any assumed convergence sequence of
future fundamentals.
It's just obviously to solve
the difference equation you need to
make an assumption as to what is
happening to fundamentals.
So in the case of this
one time change in fundamentals,
that solution takes a particularly
simple form.
The evolution of the state
variables just depends upon an
impact matrix R, which determines
the initial impact of the shocks.
So F tilde so
what are these shocks?
They're one time shocks,
the fundamentals of the model.
So that's productivity,
quality of capital,
capital market frictions,
bilateral trade frictions.
These are sort of weighted averages
of the bilateral frictions because
trade and capital market frictions
are bilateral rather than
the country characteristics.
So you have to weight them in the
right way by the initial shares.
So those are the shocks we're
feeding in.
And then R is an impact matrix
which is the initial impact it
characterizes the initial impact of
the shock on the state variables.
It just depends upon
the observed expenditure shares and
portfolio shares and
the parameters of the model.
So if you give me the expenditure
shares and portfolio shares in
the data and you give me
the parameters of the model,
I've got a closed form solution for
R. I can just calculate it.
Then after that initial impact,
how do the state variables update?
Well, they're just going to update
according to the simple AR1 process
where the matrix P here we call
the transition matrix
is going to govern the updating of
the state variables.
And again, that transition matrix
just depends upon the observed
trade shares and portfolio shares
and the parameters of the model.
And when you get that solution to
the second order
difference equation,
this transition matrix actually has
this eigen decomposable form.
And so in fact I can actually
represent it in terms of
a diagonal matrix of eigenvalues,
capital lambda here and
then the corresponding left and
right eigenvectors.
So not only do I get this
linear solution, this is obviously
in higher dimensional space because
I've got N countries, and then I'm
shocking these fundamentals.
Whereas I can actually reduce this
down to N eigenvalues and
the corresponding N eigenvectors,
so I get a lower dimensional
representation of it.
And again, I can compute all
of these things from
the observed expenditure share and
portfolio shares and parameters.
You just give me those.
I can solve for the P and
the R matrix and I can solve for
their eigenvalues and eigenvectors.
What does that mean?
It means I now can solve
the transition path of
the economy in closed form.
I don't just have a numerical
algorithm in the nonlinear model.
I can analyze it in closed form.
And so that makes it
very easy to think about.
When you change parameters,
what does that do to the speed of
convergence, the steady state?
When you take a different parameter
value, how does the dynamic
properties of the model change?
That becomes trivial because you
just simply change the parameter
and then recompute these matrices.
So it makes it very, very tractable
to characterize the properties of
the model analytically.
Okay, so let's illustrate what we
find in the last few minutes.
Make sure that I finish on time and
I want to keep us all from dinner
and drinks after the lecture.
So we implement the model
to the bilateral prey
data we used earlier, and
then also the national accounts
data from the Permwell tables.
So we match the GDP data in
the Permwell tables,
the population, labor compensation,
capital stock data in the Penwell
tables, and then the way we use
the capital holdings data is we use
it to compute shares and apportion
the Penwell table's capital stock
across all the investor countries.
So we exactly matching the national
accounts data and using the capital
holdings to construct
the unobserved wealth distribution.
And we're going to use, we're going
to build on really important work
here in the GCAT project that sort
of pioneered this sort of frontier
approach to measuring global
capital holdings, where we kind of
going to restate all the data to
deal with tax havens, restate them
for residents and nationality, and
then we make standard assumptions
about all of the parameters of
the model, discount rate,
trade elasticity and so on.
The one parameter that's.
Probably the least standard
is this investment elasticity here,
where we take a value from some of
Moto's earlier work where he's
trying to estimate that elasticity.
What do we get out
of this framework?
Well, as I mentioned earlier, it
explains this property that gravity
is not just a good property of
the trade data, but it also holds
very strongly in the capital data.
So even though we don't physically
ship stuff between countries as we
do for trading goods, if you run
a log linear gravity equation for
capital holdings,
you get an R squared pretty close
to the value for a trade equation.
And that's even true if you partial
out the fixed effects, you see very
similar explanatory power and see
similar patterns if you use Poisson
pseudo maximum likelihood as well.
What do we get out of the model by
generalizing it in this way?
Well, we actually get this sort of
really key insight,
the process of economic growth and
convergence, which is that when you
open up the Ramsey model,
you slow down the rate of
convergence to steady state.
And I'm now going
to kind of illustrate that.
I'm going to illustrate that by
showing the impulse responses of
the model with respect to
a productivity shock in a country.
And you think about the country
starting from steady state.
And I'm interested in what does
this productivity shock do
to the steady state capital labor
ratio and the endogenous variables
of the model in the.
So, yeah, so in the second panel
here, I'm going to show you
the impact of this productivity
shock in a small country.
This is Belgium that we're showing
this for in the model,
in the quantitative model.
And I'm just shocking Belgian's
productivity and solving for the
transition path to steady state.
Second panel here is
the closed economy Ramsey model.
So what happens in that model when
Belgium gets more productive?
Well, no surprises.
Steady state capital
labor ratio goes up.
Because I'm in financial autarky,
the only way I can accumulate
capital is by saving.
And so there's no immediate impact
to the productivity shock.
But I gradually
accumulate wealth over time.
And because I'm in
financial autarky,
wealth in the top line is equal to
capital in the bottom line.
And those solid blue thick dashes
give me the transition path.
Smooth convergence to the new
steady state capital labor ratio,
and wealth rises
equal to the capital stock.
Very, very standard.
So that's the standard closed
economy Ramsey model.
Everything comes through
perspiration.
I have to save in order to
respond to this productivity shock.
What about if I open up that model?
So in the second panel here,
we've Got a version of our model
where we eliminate all trade and
capital market frictions.
So there's a single global
portfolio in the world
capital markets.
There are no frictions.
Everybody holds the same
global portfolio.
And I'm now going to
shock productivity in Belgium.
What does that do to wealth
in Belgium?
Well, it does nothing because
there's a global portfolio and
Belgium is small relative to
the world economy.
So that productivity shock has
a trivial effect,
negligible effect on the returns of
that global portfolio.
But because I've got a frictionless
capital market, when I increase
productivity in capital, there's
going to be immediate reallocation
of capital towards Belgium.
So the Belgian capital stock is
going to jump immediately as this
instantaneous flow of capital,
because this is an open economy
model with no frictions in goods or
capital markets.
And then the final panel just
shows you that again, if
I let the elasticity in the capital
equation epsilon go to infinity,
and that's actually the open
economy Ramsey model where capital
is perfectly substitutable and
there are no frictions, and again
you just get this instantaneous
gapping jump in capital,
which is obviously larger when you
have a bigger capital elasticity.
So what does our model predict and
why does it give these new insights
to the growth process?
Well, our model generates
predictions in between
those extremes.
The extreme that everything's
perspiration versus the extreme
that you get all of the capital you
need from abroad.
So what happens in our
model is when there's a shock to
productivity and capital, it's
going to increase the rental rate
Belgium faces, not with sloping
supply function for capital.
So it's going to attract
a little bit more capital.
But we're not going to get
this sort of instantaneous flow
that equalizes rates of return.
Rate of return is going to go up
and there's going to be an incoming
flow of capital.
So there's initial increase in
capital, but we don't get all
the way to steady state.
We need to do some of the
adjustment through perspiration,
through accumulation, because there
are these capital market frictions.
We can't get everything from
a broad, in a frictionless way that
we could in the open economy
model without frictions.
And so from that point onwards,
there's a gradual process of
convergence to the new
steady state.
What I've done in the second panel
is I've overlaid the dynamics from
our model from this far left panel
as the blue
purple thin dashed line here.
What do you see when you
compare our model to
the Odling Henry Ramsey model?
Well, you see,
we get this immediate reallocation
which dampens down the impact of
the productivity shock on
differences in rates of return.
And then you get convergence to
the new steady state.
So because you get the initial
reallocation that dampens down
the variation in rates of return,
the convergence to steady state
is actually slower.
You cut this line from above and
then remain below it as you
gradually converge towards
steady state.
And so opening up this model,
allowing for these capital flows
generically gives you slower
convergence towards steady state.
And there are a couple of other
sort of forces in the model that
act in that way, which I'm getting
kind of short on time here,
but I'll just briefly mention them,
which is that as you accumulate
capital in our model and
you produce more output,
there's a negative terms of trade
effect because you're
selling differentiated goods and
because of gravity friction,
just selling them locally.
So that also tends to dampen down
rates of return to capital as you
accumulate capital and
induce a slower convergence.
And similarly,
because you face a sublet
circumstance of life function for
capital as you accumulate capital,
that continues to bid up the cost
of getting capital from abroad.
And that also acts to slow
convergence.
And so one of the key insights we
get out is that the slower
convergence to steady state and
response to this product can be
shocked.
What else do we
get out of this model?
Well, we get very,
very different predictions for
deglobalization.
I'm just going to illustrate that
for trade frictions and
then highlight that our model
also generates interesting
predictions for capital frictions.
So now here I'm showing you
the impact of an increase in, and
I'm going to focus on an increase
in US China trade frictions.
And in the left panel,
I'm going to do that in
a model with capital autarky.
So that's essentially
the closed economy Ramsey model,
just with trade between countries.
And then in the third panel,
I'm going to do that same increase
in bilateral trade frictions
between the US and China.
And here is a 50% increase in trade
frictions between them.
And I'm going to look at
that in our model where you have
open capital markets.
Let's think about what the effects
of this productivity shock are.
Well, let's start with the closed
economy Ramsey model.
Well, if we look at consumption in
the top panel,
when there's an increase in trade
frictions between US and
China, unsurprisingly, US And China
consumption drops immediately.
That's just the static welfare
losses from higher trade frictions.
There's a static welfare loss
because this is a differentiated
goods model of trade standard
ACR standard starting loss from
higher trade frictions
Some countries in the short run
actually see their consumption go
up like Mexico in this example why?
Those are those cross substitution
effects we talked about earlier
that now it's more expensive for
Chinese goods to get into the US
market so US consumers substitute
towards Mexico it's exactly that
cross substitution effect
Then what happens over time?
Well already in this Ramsey model
we've got something we don't
see in standard trade models
We've got this gradual decumulation
of wealth in the US and China why?
Because the increase in trade
frictions raises the consumption
price index which is the cost of
investment here so not only do you
get static welfare losses you raise
the cost of investment and so
you get this gradual decumulation
of wealth in the US and China and
some other countries accumulate
wealth over time like Mexico why?
Because those cross substitution
effects also increase
the return to investment and so
you get capital accumulation.
But as you notice here, we actually
get quite a different pattern
of dynamics for capital and wealth
in the US And China in our model,
once we open up capital markets.
Why? What's going on here?
Well, on impact, we again get
the same static welfare losses, and
they're bigger for China than US
because US Market is more important
for China than the Chinese
market is for the US and over time,
we get decumulation in the wealth
for the US but we actually get an
accumulation in wealth for China.
What is happening there?
Well, it's the combination of
a whole bunch of things.
One of the things that's going on
is that as China can no longer sell
its GOODS in the U.S.
those goods go back home.
That bids down local factor prices
and the local consumption price
index, which raises the return to
investment in China.
And that explains why China
starts to accumulate a little bit.
In contrast, in the us
once those higher frictions go up
between US and China,
the US loses access to all those
goods from China, its consumption
price index goes up, and that
raises the cost of investment and
leads the US to accumulate capital.
Additionally, once we're in this
world of open capital markets, now
all of a sudden you can get these
very strong third market effects
where you start to see capital
reallocating to other countries.
Why? Because when bilateral
frictions between the US and
China go up, I can now move my
capital to other countries and.
And third, serve those markets
from third countries.
And so this sort of highlights how
opening up capital markets can
really change the impact of policy
frictions, such as changes in trade
costs and changes in capital market
frictions.
And so
I'm kind of out of time here, so
I'll just try to stop there.
I know it was quite a lot and
a little bit quick in
the second half of the lecture, but
I hope that gave you a flavor of
how you can kind of take some tools
from trade and try to do some
arbitrage to bring together trade,
trade and international macro.
I think there's so
much exciting work to do here.
Trade learning from
international macro.
And there's some kind of
symbiosis between the two fields.
We tried to illustrate that by
thinking about a model.
When we kind of open up the Ramsey
model to allow for trading goods
and international capital holdings,
we try to model trading goods at a
point in time, capital holdings at
a point in time, and the endogenous
accumulation of capital over time.
We show our framework and
make sense of a number of key
features of the data.
Gravity equations for
trading capital flows, home bias,
and so on.
And they're bringing in goods and
trade market frictions.
They interact in systematic ways.
We get new insights for growth.
Conversions to steady state is
slower in our full model with open
goods and capital markets.
And we get new insights for
the impact of changes in frictions
such as trade and
capital market frictions.
And I should stop
there to stay on time.
Sorry for running over by
I think a minute or two.
Thank you very much.
