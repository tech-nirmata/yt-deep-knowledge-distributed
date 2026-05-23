---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 16521d31-40d2-425a-9781-12e970065522
source_title: "Public Micro Data"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:45:50 UTC
extractor: nlm_bulk_extract.py
---

# Public Micro Data

## NotebookLM-extracted transcript (Google's ASR + indexing)

Okay, why don't we get
started again?
So first of all, welcome back.
Hope you guys had a fun evening.
Probably you went out drinking,
we went to bed.
We're the old people.
But hopefully you had a fun
evening in Stanford today.
We have a busy day.
We start with something a little
lighter, which is this session
that is mostly about new data that
is becoming available that I think
is particularly interesting for
PhD students because it's free,
you're long on time, you have lots
of hours to work because you're not
teaching, you're not advising,
you're not doing lots of things,
but you're short on budget.
And so
public data, it's your friend.
Also, it makes it much easier to
start a project without having to
wait six months to negotiate
the contract, get the funding from
the university and all that.
And since you have the low small
numbers in number of projects that
you can try for your dissertation,
something fast where you can
quickly figure out whether there
might be results in there that
you want or not even just being
able to inspect what's in the data,
it's a huge advantage.
Then we're going to
switch to something very different.
So Melissa will come in and
give the methodological lecture
before and after lunch and
she'll stay for lunch.
So she's going to talk about
her deep learning research agenda.
And then she will cover a new paper
that is thinking hard about how do
we do inference with
outputs of these models.
And that will bring us to the last
session that is going to pick up
a little bit on that because we'll
do an applied paper in geoeconomics
using very much of those methods.
But then it's also going to go in
different directions for
the economics.
So that's the plan for today.
Okay, so why don't we get started
with this one,
which is public microdata.
And first let me say Bruno Canavani
was part of the GCAP Lab,
he's a PhD student at Columbia,
is really the hero that put all
of this together.
So if you have questions,
contacting Bruno is the way to go.
And Jesse, who's my partner in
crime at gcap, the two of them
really led putting this together.
I'm presenting largely because
Jesse couldn't be here today.
So yesterday we spent a lot of time
thinking about microdata and
large scale data that that has let
us do advances in economics
by looking either at old facts and
giving them a new interpretation,
discovering that the way we were
interpreting them, for example,
in theory
was inconsistent with the data.
Once you look more carefully or
just discover entirely new facts,
places of the data where we
couldn't go before because of
the absence of the information.
But we really
focus on three things.
We focus on commercial microdata,
public macro data that is
relatively aggregate.
And I've argued that there is a lot
of good stuff that you can still do
on with the public macro data and
then administrative data.
Those are data sets, for example,
for Antonio showed you what we use
with the ECB and our collaboration.
Those are all great data.
They have advantages and
disadvantages.
But until recently, what wasn't
available was microdata that we
could just simply give to you.
And that was a big limitation
because for the reasons that I just
mentioned, one, for a PhD student,
it's a much harder access cost.
Two, you don't get to experiment
with the literature because, for
example, when I assign problem
sets, it's difficult to say.
And here's the data, you know,
maybe we can do it within
the university, given the licenses,
but certainly
we couldn't post it online.
And so one big change that has
happened in the US right now
is that microdata for
the first time is becoming
publicly available particularly.
And this, I should be careful,
is microdata for
financial positions.
Okay.
And it's a project
done by the US Government.
It's called nport.
What it really is,
you can see it here.
It's a regulation that requires
investment management companies
to disclose their holdings
systematically to the US Government
quarterly.
So these are very much
similar reports that
in the past have been collected
by commercial data providers.
Or that if you think of, for
example, the ecb,
that might be part of the reports
that the microdata gets at
the administrative level.
But the advantage of these ones is
they're publicly available.
So you can go to the data.gov
website, which if you have not
seen, it's great until it lasts.
And you can Download lots of US
government data from it with APIs.
And we pick 2025 Q2,
you have all the quarters.
You can download these things.
Now, once you download them,
what does the data look like?
It's quarterly mutual funds only.
So you're not going to find dear
hedge funds, you're not going to
find either type of investors.
But the advantage is
a fully detailed portfolio reports
on the holdings.
So you're going to have very
obvious things like the value, but
also in which currency is it.
And you're going to have full
identifiers.
So you're going to have ISINs and
Q SIPs.
That's a big deal because
it's Incusives are commercial.
So very often if you don't
have a license,
the provider might not give some
of the identifiers to you there.
They're all there.
That means that you
can potentially take this data and
match it with many other data sets
that you might have available
at the university or commercially
because you have identifiers.
Similarly, you have identifiers of
the firm, they have delay, you have
country maturity, you have a lot of
information already baked in.
And trust me, 10 years ago,
when we started these projects,
putting together that information
was heavy lifting.
The fact that it comes prepackaged,
clean to you,
it's a pretty big advantage.
You also have information
on the fund side, so
many of you might want to use for
identification strategy
variation across fund mandates.
Is it a bond fund?
Is it an equity fund?
Is it part of the same fund family?
So there's a lot
of that information.
The data is also very,
very cleanly organized overall.
So there's really two key files.
There's an accession file and
a holding id.
The accession file you want to
really think of it as is
the identity of a portfolio report.
That's also important because a
portfolio is a collection of assets
that get managed by the company.
But then it might be sold to
the investors using fund shares of
many different types of and
it might be also sold as ETFs and
as an open end mutual fund.
As an economist,
we normally think of the unit of
interest as the portfolio.
Okay.
Similarly, the holding ID file has
a lot of characteristics.
And I know that this seems trivial
to you because why wouldn't you
have all of the security
characteristics?
Is it a corporate bond, an equity?
Is it a derivative?
In what currency it is
the maturity, the coupon.
If you've ever tried to do this for
a living, get that information
accurately.
It's a heavy lifting.
So this is surprisingly good.
And we should be
grateful that the US
government is putting it together.
Now what we're doing, and
part of the reason why this is
the first year we teach this
session, is we became aware of this
data when it first came out.
Then, as usual, things take time.
But one of the things that we're
trying to do with the lab and
the summer school is to provide
some public goods.
And so the public good in this
particular case is putting together
a GitHub repository of code that
has both the data downloaded, the
data is free from the government,
but also all of the cleanup codes.
So that eventually what you get
through that is you run the code
and you get a finished data set
that is well organized and ready to
go into something like Stata.
Okay, now,
we're not quite there yet,
but hopefully soon.
And we're not using this for
our own research, so.
So part of doing this is sort of
putting it out there for
our own students, for other
people that might want to use it.
And eventually I'm sure they will
figure out that there is 10 bugs,
there is some double counting,
there is things that we
need to rearrange.
So think of it very much as an open
source project where we hope that
all of you will engage with it and
send us back quite a bit.
Questions or
things that you discover that
aren't quite right and
they need to be fixed eventually.
What does the data look like?
So, for example,
the top two positions here
come from the Vanguard Total Stock
Market Index Fund.
You can see that we have
the identifier of the fund.
They're here.
What are the securities?
They're Microsoft Corp.
And Apple Inc.
These are the accession numbers.
You can see this correspond to
the fund fund report.
So they're identical.
But then these are characteristics
of the securities, the value.
So these are for
example, the issuer lay.
Here we have the identifier of the
icing of the security, the QC for
the security, the currency and then
the currency value, which means the
amount of that security that that
particular fund holds at that date.
You can get a lot more
columns into the data set, but
these ones are essentially 90% of
the information that you will need.
If you want to start thinking about
how is this fund investing
across funds.
For example, you can see that if I
skip this position, I go down here.
This is instead the Vanguard Total
International Stock Index Fund.
They're holding Alibaba.
So Antonio talked a lot yesterday
about Alibaba and Tencent and
the Vies.
And you can see indeed that if I
look at country,
the Caymans show up and the ISIN
starts with us because the security
that the fund is buying is
listed on New York Stock Exchange.
That's pretty extraordinary to
get this public and clean.
Now the first thing you do when you
get microdata is you figure out is
it good commercial data in
particular, I'm sure that Antonio
went through it yesterday has many
advantages and some disadvantage.
The biggest disadvantage is because
there's non administrative data.
There isn't a law that says that
you have to disclose the data.
It has to be correct and
it has to be comprehensive
coverage is always an issue.
Are we getting 10% of the universe
of the funds that we get in 95%?
If we're getting 70,
is it a random sample and
we don't have to worry, or is it
skewed in particular dimensions?
And is the dimensions
in which is skewed correlated with
anything that has to do with
with the results that
we're trying to put together?
So one very obvious thing to do
when you get these data sets is
benchmark against public macro data
against the aggregates.
So here all I did is
I summed the position.
So these are all of the equities
values and
bond values in the sample.
So you can see that the one
disadvantage of this data is the
sample is Short, the legislation
that forced these disclosures is
relatively recent and it's on
the US but there's a hell of a lot
of research that you can do with
a few years of US microdata.
In particular, think of anything
that is really cross sectional,
a couple of repeated cross sections
to make sure that the results are
robust, say before COVID and after
or with some particular dates.
It's all you need.
Then you take them for a spin.
So the first thing we did
is we looked at the flow of funds.
The flow of funds is the national
statistics of the US that look at
various sectors of the economy and
how they're related to each other.
And so they include positions.
So here you can see by total
assets, this is the, in the flow of
funds, the part that gets reported
as being owned by mutual funds, the
data matches up remarkably well.
You can then split them
by equity and debt securities.
And again, that gives you
a lot of comfort that this is it.
I mean, it looks pretty complete.
Now, of course,
as you go farther down,
the biases might show up.
You can see these
are very large numbers.
So some of these gaps are pretty
substantial in dollar levels,
even if in percentage
they're relatively small.
So one of the things that we did
is, okay, let's have a look at
a few subcategories.
And so, for example, for
Treasuries, I think this came up
yesterday when we were discussing
it, you can see that import
is above the flow of funds.
For corporate and foreign bonds,
you can see they're pretty close.
In general public macro data,
you also have to worry about
you never take public micro data as
ground truth.
Why? Because
very often it's based on surveys,
very often it's based on sampling.
Not all public data is essentially
fully administrative.
Clean data microdata aggregated
up beautifully a lot of the time,
rightly so.
The statisticians
have to do imputations.
They're getting
some subsets of the data.
In the particular context of
the U.S. what is a little
disappointing is that the U.S.
doesn't have a great administrative
data set for domestic holdings,
which is somewhat shocking to me
given how big the markets are and
the fact that during the financial
crisis we discovered that who owns
what around the country
can make a large difference even to
the macro performance.
The U.S. traditionally,
Antonio went through it yesterday,
has an amazingly good data set,
way ahead of other countries,
particularly in terms of when they
started on cross border holdings,
on anything that crosses
the border.
US residents owning assets abroad
and foreign residents owning assets
in the US and by assets I
should really be careful,
I mean securities.
But domestically
that data is not as good.
So the flow of funds has many more
imputations.
And so it's not
quite the gold standard.
That's very different
from where Europe is right now.
Immediately after the sovereign
debt crisis, Europe started a big
project to know who owns every
security in the European Union.
Sorry, I should.
The monetary union and
that includes all of
the domestic positions.
So a lot of the work that Antonio
showed you yesterday that we've
been doing in collaboration with
the ECB
has been loading on that data.
So by now I would say
the European data is actually
farther ahead than U.S. data in
terms of quality because you can
look at everything cross border,
but also within the European Union
that's not true for the us.
This is the foreign data.
So I just mentioned that the cross
border data in the US is very good.
The treasury does an incredibly
good job together with the Fed in
getting the microdata and putting
together a national statistics by
aggregating the actual microdata.
And the microdata is very
comprehensive because the reporting
requirements are strict and
they're well enforced.
So one of the things that we did is
we looked at all foreign assets and
you can see that again there
are some discrepancies, but
pretty good overall.
Foreign equity and
foreign debt look pretty decent.
So this gave us a lot of comfort
that if you're benchmarking
aggregates, we're not getting
wildly off numbers.
And just to form expectations,
when you open one of these data
sets at random, that's not what
they look like, you're going to
be way off in levels.
There's going to be some very
strange, bizarre spike.
This is not what normally happens.
So these I would take as
extraordinarily good news.
Very often in the lab,
when we have young arrays come in,
one big thing is everything is
going to be off a little bit.
The lines are not going to
be perfect.
So what's big and what's small?
This small looks very good.
Bad is one line would be here and
another line would be up here.
That is not uncommon
when you're trying to look
particularly international data.
And then you have to work hard
on reconciling.
So one issue is of course
this is only mutual funds.
That was also true,
for example, of the work we did
with commercial data.
Eventually we got the insurance
companies collaborating with
the ecb, we got all investors.
But particularly when
you start with commercial data,
you're not going to have
the universe of all holders, you're
not going to cover hedge funds.
Well, you're not going to cover
some of the households.
Some pension
funds are not going to disclose.
Private equity is going
to be a problem.
That's all there.
But the fact that non bank finance.
Financial intermediation has become
so big in most of the Western world
and particularly in the US
it's sort of been a friend
to research because it turns out
that the one sector that we have
much better hopes to cover cleanly,
it's also the sector that has
become the biggest over time.
And it starts to dominate almost
everything else,
at least in terms of positions.
That doesn't mean it's the most
important for prices because whose
marginal, who knows.
But if you wanted to reconnect,
so if you wanted to recoup
the aggregate positions and
you had to pick one investor class,
you would pick the funds.
You can see it here because there's
such a big part of the data.
And this has become more and
more true as we move towards
passive investment.
And all of the ETFs and
the very simple open end funds
are sort of skyrocketed in value.
So if you think of the US
with Dodd Frank, we transfer a lot
of the security holdings away from
the banking system into
the investment management groups.
And that one for research has been
a good thing in terms of ability to
get data because the mutual funds
traditionally don't think of their
positions as being that secretive.
In fact, most of the commercial
data was originally collected
because the funds do disclose at
the end of the quarter deposition.
And so the commercial providers
were simply just
collecting the reports and
aggregating them together.
On top, they might get more private
disclosures because they have
a relationship with the fund.
But a lot of it
goes on some website somewhere and
it's a question of collecting it
timely and cleaning it.
But it's pretty important
to have a sense of the magnitudes.
But in shares,
the mutual funds are so big.
Now if you were doing domestic,
things will be a little different.
The insurance companies in the US
are big,
very large holders of some assets.
In particular, they're very big for
corporate bonds.
So depending on exactly the market
that you're looking at,
there's variation in who
are the biggest players.
But cross border and
particularly in equity,
the mutual funds are very big.
Okay, then we can go farther.
We can say, okay,
let's start looking at finer and
finer splits.
So one of the things that I would
like to teach you, even as it's
almost trivially simple, but, but
once you do it for yourself,
even things that are trivially
simple take a little bit of time to
speed up your own research.
As you start from the aggregates,
then you start going finer
and finer.
As you go finer and
finer problems start to occur and
they tend to be of Two types.
One type is that the definitions
become much more important.
You and I can say let's split
corporate bonds, agencies and
asset backed securities
seems totally no hose.
You and I will code it and we will
get different answers because
there's going to be a lot of
bonds that are going to be a little
tricky to classify and the data
sets are going to disagree.
So as you go finer and
finer, that kind of noise starts to
emerge more and more.
And so at some point when you do
the benchmarks,
you're not quite sure whether there
is a real discrepancy or
is the exact definitions that we're
using that are starting to be
a little far off.
So your margin for error and
tolerance for things being a little
far off is starting to increase
compared to the aggregates.
But here what we took the data from
TIC discloses four currencies plus
a category called other.
And we said ok, let's have a look
whether for us mutual fund holdings
of foreign debt by currency
were in the ballpark.
Now of course we studied yesterday
that US funds hold a tremendous
amount of dollars abroad.
So you can see that 75%
of the holdings are in dollars.
So what if we drop that and
we inspect a little better how
we're doing on the smaller shares?
And it's pretty good.
I mean we're pretty damn close, so
no issues there.
Now what if we said okay, I don't
want to just benchmark against
mutual funds, I want to know if I
only have the mutual funds,
how far off am I going to be
compared to the full aggregates,
including all other type
of investors that are included in
the administrative data.
And you can see that things start
to being a little bit farther off.
Namely normally there is
following type of effects.
Insurance companies
tend to be much more dollar heavy
than mutual funds.
There are asset liability matching
business, they have policies
on the liability sides, they're all
in dollar, they're looking for
dollar assets domestically and
abroad to hold against.
Would be even more true if we were
including equity.
Insurance companies
don't own a lot of equity.
So if you're summing equity and
debt, you will get the split wrong.
So one trick that you can always do
with microdata is you can think
about going down to a level of
disaggregation where data is much
more representative and
then using the aggregate data to do
the weighting.
Okay, so think about it.
For example, you might be pretty
good at getting the bond equity
split in mutual funds, but
you know that that particular
split is going to be horrible.
For insurance companies.
So if you want to go up one level,
you might want to use
the aggregate data to reweight
with the information of what
the debt equity split is for
the insurance companies.
So you can play with aggregation
to make sure that you're
maintaining a representative data
set depending on the application.
If we look at equity generally,
it's pretty good.
You can see that there is a bit of
off on the Cayman Islands, but
in general it looks pretty good.
Again, these things
are surprisingly close.
It's very important
when you do research to have
a sense of the magnitudes.
This is good news.
You're not going to get
a perfect fit.
Then the question becomes,
okay, what if we benchmark it
against the commercial data?
In particular, commercial providers
are going to also use NPOR to
validate their own data.
They're using the backend and
collecting the data.
So here what we did is security.
By security, rather than doing
some aggregation, we
went at the ISIN level and we said,
let's merge it with the commercial
data we have and see if at the ISIN
level we have a lot of agreement.
And you can see it's
remarkably close, particularly for
the large positions.
Now, this graph
cuts the data on the smallest
12.5% of the data because normally
as you go to smaller and
smaller positions, the level of
noise is going to go up a lot more.
There's a lot more misreporting of
small positions than there is on
large positions.
Think of it like everybody's going
to get largely right what they own
of Apple or Microsoft in equity,
but some obscure bond security
that they own two millions off
there might be a lot more noise.
So normally when you use
this kind of microdata,
you try to look at the results.
Also value weighting to just avoid
having the small positions by count
doing a lot of the lifting.
And you can see that there is
a bunch of noise here, but
overall it looks remarkably good.
So our own take was if you were one
of our PhD students and
you wanted to write a paper,
a great idea on microdata that
requires the U.S. this data is
totally usable and it's free.
It's a pretty large
shift in the availability of data
compared to what we've seen for
the last 10 years.
Okay, so questions?
And then I'm going to go through
an example of taking what we did
yesterday and just redoing it
with full microdata, please.
Is there anything in N word of
the song in Morningstar or
if you have have the funds?
Yes. So there are certainly misses
on either side we have not fully
investigated them.
I also suspect I have no direct
knowledge of this, but I suspect
that over time there's going to be.
Be more convergence because if I
were a competent
sort of commercial provider,
I would be looking at this data.
MorningStar, for example, two years
ago when this data first came out,
put out a report
where they were competing.
So Foxit was another large provider
of commercial data.
They're extremely good
at picking up all bits and parts of
information around the world
to make their dataset better.
So I think that that's also going
to happen naturally at this stage.
There are still differences, but we
haven't investigated them carefully
enough to give you an answer.
But you can see them here as
a bunch of.
One of the two data sets is at zero
and the other one isn't.
That little corner is telling you
that there are a few.
Are there firm identifiers that you
can hardest list?
Yes. So there are lays.
So this is quite important
because you can merge to Compustat
to real data of the firm.
There's two ways to do it.
One is to use the lays.
The other one is because you
have the qcip and the ISINs.
You can use external information
to go From QCIP and ISINs to
the firm and then use anything that
chains firm identifiers.
So I'll give you some examples.
I might want to aggregate from
the QCIP 9 to the QCIP 6,
then figure out the equity that is
issued by the firm, march that one
to a capital IQ ID because that one
also has the QCIP in there.
And then I might take that ID and
march it to something
else that I need to get to,
like a Norbis Van Dyke id.
So there's lots and
lots of those crosswalks.
It's non trivial work
in terms of you need to be careful,
but it's totally doable.
A lot of the time
we have to do these crosswalks.
Some of them are now becoming
publicly available, not all of them
precisely because many of
the identifiers are commercial and
so you can't just post them.
But that's one huge advantage
of having identifiers on both sides
on the firm and on the fund.
You might be interested.
You're more interested in.
I want to know something
about the real side of the firm.
But somebody else
might be interested in.
I want to know if
these are all funds of Vanguard.
And so the fact that you also have
that side means you can aggregate
the investors in interesting ways.
There was another question.
Two questions.
So again, quarterly since 2019.
Yeah, commercial.
So Morningstar, they have anything
on finer than quarterly data.
So a lot of modern start goes way
farther back and
also has a lot of Monthly.
When you go to monthly data
in all commercial data sets that
we've seen, there is a lot more
variation in who reports,
whether they report all months.
Generally, I would say the rule of
thumb is quarterly, pretty good Q4,
nearly perfect monthly.
You have to be careful with
how the funds are coming in and
out of the data set.
Also, when you go away from the us,
not all funds report end of month,
so you have to be careful with
the dates of the reporting
depending on what you're doing.
Second question, recovers.
So back of envelope, this is 25%.
So import has 25% of treasury
markets, 30% of equity.
Yes.
I would really think of it as,
from what we've seen so far,
import has everything you need for
mutual funds.
Then everything else is a question
of how big are mutual funds in that
particular market.
Yeah. Which you don't necessarily
need the micro data for.
So the good news is you can do
a lot of the information
on how big are mutual funds in
a particular market.
You can get it from aggregate data.
And so then the only question
becomes, is this microdata close to
the universe of mutual funds?
And so far, the answer seems to be
pretty close to yes.
I mean,
universe in this context means
if you're at 90%, you're golden.
It's not 50.
I can't tell you whether it's 85 or
94, but it's in the ballpark,
where you put a footnote saying, is
the near universe of the funds okay
for anything of this size, you're
not going to get full coverage.
Not even in the administrative
data, by the way.
It's not like
administrative data is perfect.
There's lots of little bugs in that
one, too, and
decisions that you have to make.
Okay, other questions, please.
Import and Morningstar.
We haven't looked so far.
Derivatives are notoriously
difficult.
There are a couple of papers that
have used nports on derivatives.
Some of the simpler
derivatives like four words.
So it's obvious to all of you that
are finance students, but
maybe not to those of you that
are not finance students.
Derivatives are derived security on
an underlying.
So you need a number of pieces of
information to transform them into
an equivalent exposure number.
The way to think about this is if
you've ever taken a derivative
class is as economists,
the closest thing to look at would
be the delta, which is
the derivatives of how quickly does
the value of the position
move when the underlying moves.
If you're long the stock, the delta
is mechanically one for every cent
that the underlying stock moves.
So that's your position.
But if you have a call option,
depending on how far you are from
the strike, the delta might
be very, very small if you're way
out of the money, and the delta
might be very close to one if
you're very deep into the money.
Unfortunately, almost always
the way that evoddies get reported,
it's not in that form.
They get reported
as the notional amount,
maybe the value of the contract.
Those aren't obvious objects to
look at if you want to,
for example,
combine them with a position.
The fact that I tell you that I
have a $20 million position in
a call option doesn't really tell
you my exposure, because it could
be $20 million with a delta one or
$20 million with a delta of 0.01.
And so far nobody has been able to
get clean derivatives data,
particularly for the more complex
derivative, and really transform
them in a way that you will feel
relatively comfortable,
at least on a delta basis.
Summing it up with positions on
bond and equity, it's a little
difficult enterprise because if you
think about it, you would have to
know things like the maturity,
the strike, the notional amount,
the volume at that time to compute
the implied price and all of that.
But that doesn't happen.
On top of that, our experience
has been that even that basic
information, it's either missing or
extremely incomplete,
with inconsistent reporting.
For simpler derivatives like
a forward or a currency swap,
people have done better.
And so there's some very good
papers that have gone into that
direction, but that's where
the frontier of the field is again.
For mutual funds,
you worry about slightly less.
It's not as if they do zero, but
a lot of them, for example,
that are very passive
replicating an index are not going
to do a ton of it.
The ones that are like a Pimco
sophisticated bond fund that
is doing very active trading,
it's sort of starting to push
the boundary between
a mutual fund and a hedge fund.
And their derivatives positions
are going to be very,
very meaningful in terms of their
overall risk exposure.
But so far that's, you know,
terra incognita for
all of you to do the next.
Great paper, please.
>> Speaker 2: And in general,
if they have.
Because now in
the derivatives market, there are,
there's a big chunk of trading that
is with very short maturities.
Yeah, expiry.
This would not be reported.
Right.
>> Speaker 1: So these ones
are snapshots.
So think of this as this is
the snapshot of the balance sheet
of a fund at that reporting date.
So if they have short dated
securities at that date,
they're going to be included.
But you're totally right that
the persistence of those positions
might be very different.
So you might
think that if I'm trying to get
paper on high frequency trading,
getting quarterly snapshots,
isn't that great
when you look at these big funds.
The persistent depositions is very,
very high.
And so quarterly very often.
It's great data, particularly for
those of us that are more
interested on the macro side.
Quarterly is all I need.
Very often
a few years of repeated cross
sections of annual just to make
sure that the results are correct.
It's really all I need.
But if you're doing something that
has to do much more with the
reaction to a shock, the reaction
to a monetary policy change,
then that frequency really matters.
But monthly is really the best that
you can hope for,
at least in this context.
Okay, great.
So let's take it for a spin.
So yesterday we went through this
paper, which was the first paper we
at least did using the microdata.
And in the past we would assign
problem sets for these initiatives.
In fact, they're still online
that are sort of trying to get at
that one, but
aggregating the data enough that
we're respecting all sorts of
confidentiality requirements.
And this is the first year that we
could just say, well,
here's the microdata.
Just go down the regression
the same way and see what happens.
So we had Bruno do exactly that.
And so let's look at what he did.
He took it.
Of course, there is one issue,
which is the denominator.
Remember that that paper was
looking at fraction of a security
that a particular investor owns.
Now, at the time when we wrote that
paper, we really didn't have
great data on all the amounts
outstanding of all securities.
But what we did have was mutual
funds from many, many countries.
Now, if you think of mutual funds
as being the only investor in
the world, the two are identical.
Because by market pleading, if you
sum the positions of the fund,
you will be getting the total.
Now, of course, that's wrong.
The mutual funds are first,
incomplete coverage, second,
only a part of the investor.
But you could define,
if I have all mutual funds around
the world, the heterogeneity
over the total holdings.
So that's what we did.
The denominator in that paper
was total holdings of all funds.
And then looking at
the heterogeneity by type of holder
here, you cannot do that
because you only have the US funds.
And so by now we have built
much better data on the security.
The values of security is
outstanding all over the world.
And so what we ended up doing, so
there's a tiny bit of cheating in
terms of being able to do this by
yourself with only the public data,
is we ended up dividing the
positions by the total outstanding.
Now, the good news is that data is
becoming much more routinely
available to universities,
particularly for equities,
it's trivial for debt as a, for
particular type of debt, there's
a lot more heavy lifting to do.
But for a lot of securities you can
get the amount
outstanding pretty quickly.
Okay. So bear in mind
the difference in denominators
because it's going to make the
coefficients jump because you're
dividing by a different number, but
for the rest is pretty similar.
Okay.
So I'm sure you remember this
beautiful regression from Yesterday
after seeing 24 hours of content.
So I don't have to go through it
again, but I will.
We're thinking about, for
a security C issued by patent firm
P, what fraction is held
by a particular investor,
in this case a US Investor,
a US Mutual fund,
depending on whether the currency
of that security is,
is the currency of the investor.
So in this particular context,
since we're doing a single country
is, we're asking
if the security is in dollars.
Okay. And we're
restricting to corporate bonds and
we're thinking about aggregating.
Now, the aggregation that we're
going to do for this exercise is
much worse than the original one or
the one that Antonio showed you in
the afternoon for the full papers
because we wanted to maintain it
within the public data.
So all we really did is we
aggregated to the highest
identifier within that data set.
But that's not going to
be good enough.
You would have to go
much farther and try.
A Firm might have, for example,
multiple QCIP6s and you have to
know that they're connected.
This might not be obvious and
it's a detail, but again,
if you're going to do this for
a living, these details matter.
Q SIPs
are identifiers of securities.
They have nine digits.
The last digit is a checkpoint.
So it just checks that the Q SIP is
indeed valid.
The last two
digits identify the security.
The first six.
Sorry, the two digits before
the last identify the security.
The first six identify the issuer.
Now when I say identify the issuer,
it's a bit of a misnomer there,
one of the six digits associated
with that issuer.
Because you can imagine just
mechanically, if the issuer is very
big and has issued a ton of
securities over time, is
running out of the last two digits.
So at some point they'll get a new
six digit code and they're going to
keep adding them up.
So a lot of aggregating means
taking care of those six digits and
knowing that they're related.
Here we're not going to do it.
We're going to do A much more naive
of the best first pass that we
could do to say that these are all
bonds issued by the same entity.
Okay, okay.
So here's what it looks like.
You get a very
large currency effect.
This is for a different year.
The magnitudes should be off
because we changed
the denominators, but
you find exactly the same results.
And this one
you can do by yourself.
Similarly, we could go back to the
truth tick that we did yesterday.
What if we wanted to
replicate the the classic result of
getting home bias in securities,
the idea that investors
hold much more of securities issued
by their domestic firms.
And then we can say, okay,
is that true also for currency?
And what if we put them together,
which is exactly what we
played around with yesterday and
here's the results.
One of the things that I love about
home bias is I love results where
you pick any piece of data
that is sufficiently reliable and
these things pop up.
That's what makes them
really solid.
I care a lot less that you can run
exactly the same regression,
get the four digit right.
I care that this is a result that
in whatever piece of data you look
at is a big
characteristic of the data.
It immediately comes out and
you can see that home bias is
one of them.
This is totally different data.
We're 20 years away from when
French and
Potterba wrote their papers.
And it's just such a big factor of
the data, it shows up immediately.
It's like running UIP for
exchange rates.
You run any
half a decent piece of data and
you're going to find a UAP fails.
I like those kind of facts.
Now here's currency again.
It shows up pretty strongly.
And here's when you put them
together and
you find the same effect.
Now because you're going within
group, the home coefficient
drops down and the currency
coefficient stays up there.
So this is just an example, but
it's to show you that
things that 10 years ago would have
been two years of heavy lifting
trying to get the data and
you would be at the forefront.
Now they're becoming, okay, this
took three weeks and probably will
take you a little longer because
we've done this for a long time so
we know where the bodies are.
But part of putting these
repositories together is to fast
forward you and say, look,
if you want to write a dissertation
next year and you need microdata,
here you go, it's there,
it's clean, somebody told you that
it's actually half decent.
And hopefully we get to hear from
you all the little things that
are wrong in the cleaning codes or
you might find particular
dimensions and you were asking me
yesterday about the Treasuries and
NPOR being above we'll look at it.
It could be that the flow of funds
is using some
survey that is incomplete and
is the flow of funds that is off.
It could be that NPORT has some
double counting some values that
are wrong that are particularly
big in Treasuries and
we'll have to look at them But
I think collectively I suspect this
data is going to become clean and
routine the way the 13 Fs for
example have been so I'm going to
stop here and see if there are any
questions but hopefully for
those of you that want to do this
kind of work this will save you six
months of your life six unpleasant
months of your life please.
So I think what these ones do is
that they counted both but
this data does not include
the money market funds.
The Morningstar data has them but
I think we excluded them
in the benchmarks
SA.
