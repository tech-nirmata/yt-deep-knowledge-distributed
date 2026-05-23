---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 7de120b3-cd67-4af1-a6ba-4401ca252edb
source_title: "AI-Driven Supply Chain Optimization at JD.com"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:32:31 UTC
extractor: nlm_bulk_extract.py
---

# AI-Driven Supply Chain Optimization at JD.com

## NotebookLM-extracted transcript (Google's ASR + indexing)

Good morning, good afternoon,
and good evening to all of you and
welcome to our Value Chain
Innovation Speaker Series.
My name is Barchi Gillai and
I'm the Associate Director of the
Value Chain Innovation Initiative
at Stanford Graduate School of
Business.
Today we're excited to host two
guest speakers from JD.com,
which is China's largest retailer
by revenue and a leading technology
and service provider
with supply chain at its core.
Our speakers are Professor Max
Shen, who is the Chief Scientist
and a Vice President @JD.com in
addition to being the Vice
President and Pro Vice Chancellor
at the University of Hong Kong.
And Dr. Yongzhi Qi, who is
the company's Technical Director of
Supply Chain Algorithms and
also serves as a Guest Professor at
the University of Hong Kong.
Together, they will provide
an overview of the AI-driven
supply chain optimization solutions
the company has developed.
They will also highlight
the powerful capabilities enabled
by integrating AI with
operations research methodologies,
and share their perspectives on
the key prerequisites for
successful AI implementations.
Moderating the discussion is
Haim Mendelson, who is a professor
at the Stanford Graduate School of
Business, and
the Faculty Director of the Value
Chain Innovation Initiative.
>> Speaker 3: Thank you very much
Barchi, Max Shen, Yongzhi, it's a
great pleasure to have you with us.
Let's go ahead with your
presentation and everybody is
welcome to ask questions during the
presentation using the Q and A box.
What I'll then do is combine these
questions with my own questions to
moderate the discussion.
This is a very interesting topic
and we may well have more questions
than time to answer all of them, so
we apologize in advance
if some of the questions don't
show up in the discussion.
Thank you very much,
go ahead please.
>> Speaker 1: Good morning,
good afternoon,
good evening everyone.
Thank you for being here today,
it is a great honor to have the
opportunity to share with you some
exciting developments in the field
of supply chain optimization.
Today's presentation will be
a joint effort between
Professor Shen and our team.
I will start by covering the first
part of our discussion which
provides an overview of JD.com and
set some background.
Then Professor Shen will take over
to dive deeper into the specific
application of AI.
We are excited to share our
insights with you today and look
forward to a fruitful discussion.
I will now begin with the first
part of Pre Listening.
The first question is,
who is JD.com?
JD.com is also known as JINGDONG
or JD.
GINGDONG, is the largest retailer
by revenue in China and we are also
a leading supply chain based
technology and service provider.
We serve about 600 million
users and
we have over 10 million products in
our first party retail business.
Our operations are supported by
more than 1,500 self operated
warehouses, and we are proud to
fulfill over 90% of orders on
the same day or the next day.
As for our inventory, we maintain
a 13 day turnover ensuring high
efficiency in our operations.
In 2024 our net revenue exceeded
US$115 billion,
reflecting the scale and
success of our business.
However, with such an extensive
network and
wide ranging operations,
we encountered numerous challenges.
They include, fluctuating demand,
particularly during peak certain
events like the 618 shopping
festival, the China largest e
commerce festival that unleashes
massive customer demand and
pose significant challenges to our
supply chain operations.
Facing such big promotion periods,
we need to commence preparations
months in advance,
updating our forecasts and plans.
This involves assessing the impact
of various promotions on demand,
coordinating with suppliers on
production, and inventory, and
striving to meet the customer needs
while digitally avoiding overstock
squeezing.
JD.com boasts a diverse range of
business operations,
we have our retail business,
we have our logistical business as
well.
We have technology infrastructure,
like our cloud service.
For instance, JD Retail Company
focuses on the retail sector,
providing a platform that connects
brands and customers,
serving over 600 million users.
JD Logistics offers delivery
services, ensuring that goods sold
to customers are delivered safely
and efficiently.
JD Technology provides foundational
service and solutions such as,
cloud services and
financial services.
Of course,
we also have JD Property, JD House
and other business segments.
JD Ecosystem thrives on cross
Sector innovations, turning supply
chain more efficient.
Okay, let's look at
the Conventional Supply Chain Model
which has been the backbone of many
industries for years.
The traditional supply chain
process involves several key
the marketing, the planning,
inventory, and the fulfillment.
I think conventional supply chains
often face challenges such as
fragmented systems,
manual processes, and
a lack of trust in data.
These limitations can lead to
inefficiencies, miscommunication,
and slow response times.
Supply chains are inheriting
the integrated process and
many companies aspire to manage
them as a unified system, however,
existing system capabilities
offering full sort of risk.
Typically, supply chains are
divided into multiple segments with
each segment handled by the same
department, so online or offline
communication and operations.
Each operation relies on separate
system, making it difficult to
ensure comprehensive alignment and
flow of data and
information between these systems.
As we move forward, our system will
become more interactive,
integrated and collaborative.
It is an AI-based system that
leverages artificial intelligence
such as, planning, replenishment,
and order fulfillment.
One of the key advantages of
this system is its ability to
dynamically combine these
capabilities based on the specific
needs of the users, ensuring that
we can achieve global optimization
across the entire supply chain when
it is adjusting inventory.
Fulfilling orders or optimizing
the flow of goods, the system can
quickly adopt to changing demands.
In the future, the user's requests
will no longer be handled through
traditional interfaces.
Instead, all interactions will be
carried out through a chat-bot here
within the systems, enabling a more
intuitive and efficient way for
users to communicate their needs.
The system will be able to
understand and respond to these
requests in due time, providing its
solutions that are fully
coordinated and optimized.
This new approach will make our
supply chain more agile and
responsive, allowing us to improve
efficiencies and
better meet customer demands in
a rapidly changing market.
Now, Professor Shen sell the second
part of the AI applications we
have.
>> Speaker 2: Okay, thank you
Yongzhi for the introduction.
So for folks, I think you probably
for the Stanford folks and also for
the city Hawaii folks,
jd.com used to be a neighbor.
We were at Mountain View a few
years ago.
I think we also have interactions
with Stanford student and
business school during that time.
But now most of the [COUGH]
technical people move back
to Beijing.
So if you don't really understand
jd.com, I can just give you
a simple example.
So you can think of JD as Amazon
plus UPS and now even/doordash
because we are entering into
the food delivery business now.
So it's really, really a huge,
huge company.
We have hundreds of thousands of
people working for Jd.com as
Yongzhi mentioned here, when I
start working with jd.com, we have
a lot of very traditional planning,
forecasting, optimization problems.
But recently we are really proud of
this AI technology, especially this
chat bot thing, because if you look
at the whole supply chain as shown
in the PowerPoint,
it's really important to have
a good forecasting.
And then
you have to have interactions
otherwise all the stakeholders will
not be on the same page.
So this interactive communication
explaining why we make decisions
this way or that way and
then eventually come up with
a system optimization is really,
really important for all companies.
So let me dive deeper into some
of these planning tools.
So [COUGH]
in fact this is the second part.
This is kind of the interactive
part.
And also one of the problem we have
working as a supply chain optimizer
is that sometimes it's really
difficult to do this because you
need to write code and then collect
data and then run something and
then explain to people.
But now with our AI chatbot,
we can actually just type in some
questions or even better,
you can just say it.
You can just say that what is my
inventory level for some products?
And then what is my future sales
for the next three months.
And then our AI tools will go to
different databases,
different planning algorithms to
answer these questions.
I don't have time to go into all
the details, but once you enter
something to the chatbot window,
[COUGH] it will start to kind of
understand your question.
Is this one sentence or
two sentence?
Do you have what if?
What exactly are you looking for?
And then we'll call different
agents.
The agents I've mentioned before,
including forecasting,
inventory planning,
optimization, there are thousands
of these different agents and then
they will work together to come up
with the answers to your question.
That's the interactive part.
I just want to show
the exciting part.
But before that, we also have
to do a very good forecasting so
that different units, different
department can be on the same page.
And this is something that we
are really proud of too because we
do have a lot of private data on
our platform.
We have 600 million active users.
So this user's activity generates
so many private but
very rich data for us to analyze.
We also get a lot of public data
from the weather, the market,
treating the tariff war,
[LAUGH] all these kind of things
because this will influence our
sales and forecasting.
And then actually,
very interestingly, we want to talk
about this synthetic data.
This is actually some data we
dive deeper into all of
our past transactions and then
we learn from these transactions.
We understand why some of
the actions achieve better results
and then those kind of data will
be used for future forecasting,
generation, future optimization.
So in the end,
I think it's a kind of a teamwork
among different engineers.
We have team that work on data
cleaning, just get the data ready
for business and also for
algorithm engineering.
And then we try to make the data
richer and richer to eventually
have better results.
So this is what I just said
earlier, but I just want to show
you that now we also have the self
learning capability.
So as I introduced in my last
slide, we did this all by ourselves
at the beginning.
But then when AI tool pick up what
we learned from historical data,
they can try to do self learning.
So in the end we have almost 15%
increase in prediction accuracy.
And we actually have a technical
paper on this where we talk about
all the detail, how we use
the patch neural network, how do we
actually find the patterns among
different products,
different neighbors.
All these details are in the paper,
I can share with you later.
So [COUGH] let me just give you
a couple of examples what we talked
about earlier.
We talk about interactive,
we talk about [COUGH] forecasting,
but in the end you need to convince
all the different stakeholders to
use your results, right?
So we typically face this problem
that we have all the fancy tools
and then it spit out a number.
This is the forecasting for
iPhone 17 in the year 2027.
But how do we get this number,
right?
Why people should trust you with
this number?
In the past, I think all of us were
pretty bad in explaining this
because it's such a complex tool.
You consider hundreds of different
features, whether discount
marketing condition, what your
competitor has been doing,
is it holiday, all these things
had to be considered.
So you cannot explain clearly
the number 80 book was because
of A and B, right?
But this is not good,
because when you try to convince
your salespeople or
your marketing people this number,
you have to make them believe this
number, right?
So based on this background,
actually we have this explainable
AI now.
The rough idea is to try to explain
most of the important factors to
all the stakeholders so that they
can kind of agree with you for
your promotion plan or
for your inventory planning.
If you look on the right hand side,
normally for any products, right,
you would have a baseline forecast.
So this is mainly based on
historical data or
some of the intelligence you have.
But then there are, as I
mentioned earlier, there are many,
many different factors
will influence the final outcome.
So we would do some kind of
analysis to identify a few major
factors.
For example, promotion,
seasonality, market training.
We don't tend to have too many of
them, maybe just five, six, seven,
that kind of numbers.
Hopefully, this few major factors
can contribute to majority of
the final forecasting quantity,
right?
So then we list out all these
numbers.
We have a range for
this which is more accurate.
We don't just spit out one number,
we have a range.
So that now if you put all
the different teams for marketing,
production, sales, transportation.
They will understand the movement
from all these numbers and then
kind of agree with you the kind of
rough number.
And this is another example for
the kind of explainable AI.
In China, in fact, as Yongzhi
mentioned, we have so many holidays
for e-commerce companies.
We have 6, 18, we have Double 11.
November 11th is probably one of
the largest festival for
people to buy.
It's even bigger than Black Friday.
People just go online to buy,
especially for your single friend.
The reason we have November 11th
is we have all the wines.
That means you have wine.
You don't have your girlfriend, or
boyfriend, or couple, right?
So we feel pity on you,
then we buy things for you.
That's how we call Double 11
festival.
But then it became such
a phenomenal marketing event that
we buy for everybody, even you have
a girlfriend or boyfriend.
So during this sales event,
a lot of companies on our platform
actually have a target.
They say, I want to sell 5 million.
Their company may have 10 million
or 3 million, whatever,
they come up with number, right?
Then they will come work with us to
see how they can reach this number,
right?
So we look at historical
performance.
That's kind of the demand baseline.
So for this particular example,
with 8Million there, right?
[COUGH] So
if this company want to sell for
10Million, they will have to come
up with a strategy for them, right?
So with 8 million,
we think this is not enough.
There might be demand fluctuation,
which is arranged in the order of
1Million.
And then we have to rule
out promotion strategies.
So we would come up with three
different strategies, right?
Plan S, plan A, plan B,
all with different outcomes, but
also with different costs.
So you can see that promotion plan
S actually can move your
sales up by 1.5Million.
And then promotion plan B only give
you 0.5Million, right?
So we would then present this kind
of strategy to this company.
And then we will also analyze
the weather, rainstorm,
sport events, many other things.
And then we will give them three
options, right,
the plan 1 and 2 and 3.
So basically, one of
the plants have very high sales and
this is maybe what they wanted.
But also they have to spend more
money on this, right?
So we just present all these things
to them,
they will come along with us.
Otherwise, you just tell them,
look, you want 10Million,
no problem,
you pay me half a million,
I will give you 10Million.
They won't believe in you.
But now with this kind of analysis,
things become much easier to
communicate.
So let me move on to, let me see.
Why is not moving?
Okay, so now, this is the third
problem I mentioned,
right the optimization part.
Hopefully many of
the audience know optimization,
what I'm talking about.
So for truck delivery, for
inventory planning,
all this, you need to optimize
your resources and then achieve
the maximal outcome benefit, right?
But in the past, whichever company
you work for, you have to write so
many codes and clean so
many data and fit all these things
to the optimization engine.
And you probably need maybe a PC or
master degree from Stanford to do
this.
But there are many problems with
this approach.
First of all, it's so
kind of difficult to do this,
right?
You need to write the code, and you
have to write an elegant code and
you have to run fast.
Otherwise, you wait for
the solution for three days,
it doesn't mean anything.
And then you need to have the right
kind of data to fit into
this optimization model.
If your data is garbage, then your
outcome won't be very good.
Certainly, many of the parameters
you have to kind of take a guess.
It's not really kind of dynamic,
real time.
So even though you solve
the problem, sometimes you cannot
convince people on the ground
to use these results.
So now, with our interactive or
operational research and
large language platform,
we can real timely fine tune all
these data inputs and solutions so
that we don't need a Stanford PhD.
I think anybody can say that your
wish can do this.
For example, I want to give you
an example first.
So for example,
you have several warehouses and
you want to [COUGH] basically place
an order of 1000 units.
And then
each warehouse have a capacity.
And the cost of transporting and
storage at different locations
are also different, right?
So this is a very typical
optimization problem.
And then, as I mentioned earlier,
you can,
a PhD from a top school can write
this and solve the problem.
But the problem is first of all,
writing the code is difficult.
Secondly, all these parameters may
not be very accurate based on what
kind of truck you are getting from
the market.
The cost might be different too.
So, all these things, don't worry.
We can actually go back to this
ChatBox, just say look,
I have this situation.
And please find a plan for
me to order 1,000 units and
put in into my warehouses using
the cheapest method, right?
So with this it will convert your
English into mathematical model.
With the mathematical model then,
AI can automatically generate
the code for the problem, and then,
we'll go directly grab the data
that are useful for this particular
problem, and then solve the problem
with the solution.
In fact,
you can also make what if analysis.
So this is what AI is very good at.
You can just say that,
by the way, I think the capacity in
one of the warehouses is changing
to this number or the truck deliver
product to one of the warehouses,
it broke down or things like that,
it can quickly resolve the problem.
So, I guess so this is what I just
mentioned before all the details.
So, I guess my time is running out.
I'll just quickly summarize,
kind of share with you in the past
few years how we achieve all this.
I think it's really important to
have a good team, and that's why
we located our tech R and D center
next to Stanford a few years ago.
And then there I think we have
roughly 200 people with PhD from
Stanford, MIT, Berkeley.
And then, now I think even though
we're back in Beijing,
we're still looking for
talented people to work on this
interesting e commerce problems.
And then, it's really, really
important to have the leadership
change to accommodate AI.
Because you probably all know that
Eric engineer might come up with
a very good [INAUDIBLE] but he or
she might have a really hard time
setting this to marketing people
procurement team.
Now we actually in JD.com we have
this organizational change very
flat, so, we'll have the engineer,
whatever engineer working
directly with a business side.
Whoever can make the money will
have the sake, right?
So, I think now with this flighting
organization, the AI engineering
can link directly the performance
of the algorithm to the outcome of
the sales.
If you can make a change,
people will listen to you and
you have to say in the business.
And then, to make this happen as I
mentioned before, I think JD have
so much data for us to play, and
then, to train our big AI model.
That's why our model become
better and better.
And also with different scenarios.
We have hundreds of millions of
different SKUs in our warehouses.
So with so
many different scenarios, we can
just look at inventory problems.
We can have classification on long
tail products, frozen products,
and some products that won't
go until you have a sale.
So there are all the different
characteristics of these products,
and we can have rich data for
each scenario.
And actually,
if you can see the picture,
we worked with Professor Hau Lee
from your school over the last few
years, on many of the JD problems.
And then we have won several major
awards from Informs,
Edelman finalist award.
And last year we have the INFORMS
prize.
This is the highest award for
an organization that apply OI and
data analytics to their daily
problems.
And then last year we also won
the Wagner prize.
This is for
the technical problems solving.
Okay, so, I cannot say enough for
this but@gd.com actually they go to
different universities to hire,
they call genius, but
basically smart kids, right?
So, I think their pay is very high.
At one time I was tempted to join
this team too.
But with all these talents,
they can actually work together,
solve many of the heart problems.
And then now they are looking for
talents again,
anybody in the audience, if you
have a smart kid in your family or
that, can encourage them
to apply to this program.
So, with that I will quickly
summarize.
I think the last few years,
AI is coming at us and
people call this AI Tsunami.
It's just coming so fast,
we are barely surviving.
I think one of
the important things is that,
you have to do a lot of trade offs.
There are a lot of big models, but
it costs so much, and
it's also not economical or
environmentally friendly.
But our belief is that
you don't have to have those kinds
of big models.
You can actually have a kind of
a small model that utilize your
experience and
your data to solve your problem.
Of course, occasionally,
you might need to get help from
those big models.
But I think the key factor is that
whether it's effective for
your problem and then whether you
can run very efficient, very fast,
and then, how much it costs you.
So we achieve kind of a nice
balance among these three major
factors.
That's why we are moving forward.
The AI team, the team is growing
and I think it's bringing a lot of
benefits to the company already.
So with that,
I guess I will stop here.
I guess we are doing fine on time.
I'll go back
to Professor Mendelson.
>> Speaker 2: Thank you very much,
this is very interesting, and
I'll start with a question from our
audience, and people are invited to
submit additional questions.
The question is about live
streaming, and the question is
about what is JD's view on
the future of live streaming?
Is a customer interaction mode
in China,
and what is it doing about that?
>> Speaker 1: Okay, so
maybe I can talk about this.
This is a phenomenon, I'm not sure
people in the Bay Area notice this,
but in China, if you look pretty or
you look ugly or whatever,
you attract audience.
You can go on.
On a show or whatever you can sell,
you can eat or you can drink, or
you can just sell
some of the product, is becoming
a really big phenomenon.
I think actually at one time,
probably last year or
a couple years ago,
people were telling us that this
kind of model will overtake gd.com
because one night you can have
millions of dollars of sales.
So we were quite worried at
that time.
But then if
you look at the whole supply chain,
I think this phenomenon, I mean,
it will still continue.
But their supply chain,
they don't have a supply chain.
So for people who work on supply
chain, this is a huge burden for
everybody who work with them.
Last month there's no sales.
Then suddenly tonight, their middle
item need to be shipped out
from different warehouses,
working with different company.
So unless they figure out how to do
this more efficiently.
As I mentioned, performance,
cost, and
effectiveness has to be considered.
I think, people in China, many
people go with this kind of sales.
Maybe at that night they
buy something out of blow.
I think they being attracted by
the looks of the people.
But then they may regret for
daily life, right?
You go to Costco,
you buy things you need,
that kind of buy sells.
And many of my friends do that too,
end up in their own garage or
another bedroom.
I'm not sure how to look at it.
I mean, for surely,
they are impacting our business,
but I think now, even the CEO of
gd.com did this too last year or
earlier this year.
It worked really well.
So we will have to take the good
part of this phenomenon,
embed this into our supply chain
without our powerful supply chain.
I think for whoever are doing this,
it's a very good business model.
You look at why did you make
millions, but maybe another day you
don't make any money at all, right?
>> Speaker 2: Great, thank you
very much.
Let's go into another area which is
the effect of AI on the larger
organization.
So we talked about the smaller
organization that makes all of this
happen.
But given the capabilities
of the technology, what happens is
that there is going to be at least
in the future, a bigger impact on
the structure of the entire
organization, given the ability to
automate many of the functions and
to get very quick feedback.
So the whole structure is going to
change to one where people work
with AI to make decisions that were
made by people earlier.
So two questions.
One is kind of what is your broader
view on the organizational impact
of these AI combined with OR
models?
And second,
how is it going to affect JD,
let's say on a five-year horizon.
>> Speaker 1: Yes,
I mean this is a really important
question.
Thank you for asking.
I think this is impacting every
company, right?
Many of the small firms were
thinking about putting out AI team
to do this too.
But at gd.com, I think we have
hundreds of people to do this.
But we have the goal of maybe
sharing some of our results with
smaller companies,
media-sized companies who actually
work with us.
We can share with API, we can share
some of the capabilities, they can
plug in our ecosystem and then do
the things we just talked about.
But for the whole company, I think
we have to have very effective
leadership from the top.
Whenever you have some
new technology coming in,
the resistance, actually,
many come from the leadership
because they don't know this.
Many of the senior leadership,
they have been in the business for
20, 30 years,
they don't see these things.
They are not confident, they will
actually do this very slowly.
But I think fortunately enough
for gd.com,
our senior management team is kind
of embracing this opportunity.
So that's why I think they
are quickly hiring different
fronts of optimization,
data analysts, and AI people.
How will this work?
To be frank with you, they don't
know how this will pan out, but
they know this is
the future, right?
So, for the R&D center in
Mountain View a few years ago,
as I mentioned earlier,
we have 200 people.
They have PhD from Stanford, MIT,
they study computer science, double
E, triple E, operation, research,
mathematics, even biology.
They put people together.
Similar culture is, if you look at
Google and Amazon, this company,
they hire talents, right?
With these talented people,
eventually we figure out,
with the guidance from senior
management, we figure out how
to do this most efficiently.
You probably know that many of
the companies spend a lot of money
to buy hardware.
But I think that's not the most
important thing.
The culture change.
The people you hire into
your organization is the key for
you to go this route.
In the worst case, even though you
don't have all these capability
hardware, you can always use cloud
service from other companies.
So buying those hardware is not
the most important thing.
Training people make them on
the same page is very important.
So I think that's the kind of
the first part of your question.
And secondly, I think with gd.com
we now have this culture that we
need to look for more talents.
So our CEO Yuan was touring
different universities,
trying to hire people.
So I think we are all ready.
I think the post AI and
optimization has been increasing
steadily in the past.
So it's a trend,
we cannot avoid that.
The competition is whether you can
get the right kind of people to
work for them.
>> Speaker 1: Great, thank
you very much.
And let's talk about
the smaller organization,
the 200-person organization.
What is the process that you go
through to select people into
the organization, and what
are the types of attributes that
you're looking for in an effective
member of your organization?
Your 200 person organization.
>> Speaker 1: So I assume you're
talking about a logistic or
supply chain company, right?
Because different company might be
looking for different things.
I think in all these companies,
normally you have a forecasting
team, you have a transportation
team, you have an inventory team,
sales team, right?
And then another team more closely
related to the.
The business consumers.
So for these five teams, I
think when we look at this problem,
we need to find somebody who can
work with all these five teams.
Not that they can go there and
do their daily work, but
who can communicate with them well?
So, for example, in our field too,
we used to just hire IE, OM,
PhDs, but then recently many of
the companies have hired computer
scientists, right?
So why we do that?
Because these people actually
change our thinking process, right?
They tell us it's very important
not look at the so-called optimal
solution because the optimal
solution in some
scenarios doesn't mean much.
You need to make it work
first of all.
Secondly, you need to make it work
fast, right?
So I think that kind of people, if
you bring to your organization can
change people's thinking process.
Of course, this has to be blessed
by your management, otherwise it
will be kicked out very quickly,
right?
People might protect their own
turf, only hire their own kind of
business people, or IE people.
So I think that's really important.
Somebody who can change the culture
and thinking process, right?
Then the management need to make
these people be in charge of
something.
They cannot be the engineer who
give you a solution and
then other people implement this.
You have to make them hopefully
interact directly with your
customer, and then work directly
with your business side, so
they can see these
things are working, right?
By working directly,
sometimes you need maybe help
from the other five teams.
But I think this is a really
important process that everybody
can see this is working, and
then now eventually,
people wanting to work with you to
make their own units better.
>> Speaker 2: So if you have two
people, there are two ways to kind
of create those teams.
One is to say we take the best
athlete on each dimension on the
software dimension, we get the best
athlete on the other dimension,
and we mix them together, and
that's how we get results.
And the other approach is to say
let's take well-rounded people, and
we're going to compromise a little
bit on their software skills.
But we're going to trade
off these different skills, and
we want to have people who can do
all three things.
Which of the two would you prefer?
>> Speaker 1: I think we need both,
but in the beginning,
second approach is very important.
If you are the best ethics,
they don't talk to each other,
that's the end of it, right?
[LAUGH] So you need to have
the kind of this where are wrong
people to come in first, and then
if everybody is on the same page,
they understand that we need to do
this, then you can go out and
find the best people
to do a particular thing.
But if you do the other way around,
I think normally will lead to
a disaster.
>> Speaker 2: Great,
so I'm going to move to a more
technical dimension.
One of the key, I think,
advantages of your approach is that
you have explainable AI.
It's not a black box so people can
understand where it came from.
It was not entirely clear to me
when you explain it, the question
is that an interactive explanation
or when I get the results,
I can see the weights are this and
this, and this.
And then I can come back to
the system and
have another prompt and so on.
>> Speaker 2: Yeah. >> More
generally, how does that process
work of reconciling the automated
recommendations from the system, or
maybe their decisions in some
cases, and what domain experts want
to do. How do you do that?
How do you manage that?
>> Speaker 1: Yeah, great question,
for the two different approaches,
I think we do both of them
depending on whether it's something
that need buy-in from
different people, right? So you
probably do production planning,
material planning, all this.
In the textbook, we just make up
a number and tell everybody to do
it. But in practice we think,
especially nowadays, demand keep on
changing and all that.
You need almost real-time to get
different units on the same page.
So this way,
this one is that we have to do very
interactive discussion about this.
For example,
one of the truck breakdown, one of
the warehouses have a strike,
this kind of thing.
Then you need to adjust your number
like with this,
so before this disruption happens,
we do get people in the same room.
We say, look, this is,
as I explained before,
those are the major factors.
We think next month our total
inventory ordering should
be this number.
And then hopefully everybody will
be in the same page.
Even if not, you remember,
we have a range, right?
So you can adjust the range to
hopefully get everybody in
the same box.
But we try to make this range as
small as possible.
And then if somebody strongly
disbelieves this, finally,
just like machine learning,
you have to take down this.
His belief,
he believes next year some of
the things will go over the roof.
Eventually, you walked and then,
after many dinner points,
you have credit for this,
each person, right?
And then their input will be
weighted.
So it's a really cultural thing,
but with everybody on the same
page, you can react to disruptions
or abnormal events much quickly.
So that's kind of the first part.
Do you have a second part of
the question.
>> Speaker 2: So I think they're
related and I think you
answered both of them already.
So that's great.
Different question, how do you
generate the synthetic data, and
how do you know that it works well?
>> Speaker 1: Yes, [LAUGH] this
is actually technical, right?
So in fact,
to tell the truth, when we first
work on our large model using our
own data,
it actually did not work well.
Why?
Because there are so
many dirty data.
[LAUGH] If you look at raw data,
many of the data are not proper and
missing data, it's not coherent,
and all that.
So then we plug in the public data,
it doesn't have much.
So now the AI plays a role.
So we have been ordering this
product for three years, right?
We will look back at different
ordering and see what happens if
some of the decisions,
some of the ordering quantity
bringing good results.
We are learning all this,
then we can generate some
of the data that are similar.
You change some conditions and
they will spit out similar answer.
We put this kind of data into
the system, those are the good
things you can learn.
And then after we get rid of
the bad data from the original
data, eventually the result is much
better.
>> Speaker 2: Right, so
we have an audience question.
The question is.
>> Okay.
>> How is J.D.
dealing with the US tariffs?
And I will broaden the question and
ask, think about this.
Is an exogenous shock.
How do you feed the shock like that
into the system?
>> Speaker 2: So, I guess,
that's a political question.
I guess,
our leadership- >> Speaker 1: Yeah,
we can focus on my question.
>> Speaker 2: Yeah, but this is,
as you mentioned,
you can think of this as a huge
disruption to your system, right?
So in fact, at gd.com,
something you probably don't know,
I didn't share with you yet.
In a big city in China, in Beijing,
many of the big cities, if you
order something in the morning,
before 10am, you will get it in
the afternoon, right?
So I live in the Bay Area for
20 years,
I never have this kind of luxury
of getting this product same day,
unless you pay 200 bucks, right?
So how come, we can do this?
Actually, that's the slackness
in the system, okay?
And second factor is that,
we actually do a very good
inventory repositioning.
So before Professor Mendelson
order, we know, look at your
historical order, you probably want
to buy iPhone in September.
We probably will ship this iPhone
next to you, okay?
So with this,
what I'm trying to say that,
we have so much data intelligence.
And we try to protect the future
disruption.
Tariff is one thing, but
there's snowstorms, there are bad
weather here and there.
We can easily buffer a few days,
up to a week or two weeks,
the disruption.
In fact, our inventory level is
very high in the overall system.
That's why we can ship products
from different warehouses, from
the closest warehouse to you, so
that it can reach you in one day.
So we are well planned.
We do have taken into consideration
of this kind of disruption, but
not at the tariff level.
It may be much longer than a few
weeks.
But if it's a few weeks,
couple of months, I think, we have
a very efficient way to do this.
>> Speaker 1: And do you simulate
future scenarios going out
years and
years to do long range planning?
>> Speaker 2: We do, we have a very
good simulator, actually.
It's almost like a digital twin,
it's like a real system.
We stress test many of
the different scenarios.
But for a business to run well,
you have to consider cost.
So we would make it the right kind
of balance.
We will make sure we have
the resilient supply chain.
But on the other hand, we don't
want to incur too much cost.
So that's a business decision from
the senior management.
>> Speaker 1: So I want to go back
to one of the things that you said.
You talked about the ability to
predict people's behavior based on
their past performance.
And I'm assuming that,
for statistical aggregates of
many people,
you can get a very good forecast.
Now, can you actually do that at
an individual level?
And can you remind the person, you
forgot to order your toothpaste?
>> Speaker 2: I mean, certainly,
if you have enough data,
you can do a lot of things, right?
So we can, yes, at the beginning,
we do this category thing.
A girl working in a big firm with,
living in a downtown area,
her buying patent would be very
different from somebody who live
in the rural area.
But we have the membership thing.
Amazon has a membership too.
If you have membership with us,
we know your history.
And with so many data points and
similar purchasing patents,
you're grouped, we can actually
pretty well forecast your
future behaviors [LAUGH].
It will surprise you [LAUGH].
>> Speaker 1: So you have a
physical twin of each
customer [LAUGH].
>> Speaker 2: In fact, we have
a campaign- >> I'm sorry, digital
twin [LAUGH] >> Speaker 2: So,
in fact, we have a kind of campaign
several years ago,
called 1,000 people, 1,000 faces.
So that means, we will, basically,
draw every person's behavior like
we draw their face.
You can immediately see,
they are different.
>> Speaker 1: And so, this is very
impressive.
Have you ever thought about selling
this software,
adding a software vertical or
service of that type, AI service to
one of JD's businesses?
>> Speaker 2: Certainly, I mean,
this is, certainly,
the planning, right?
As of now, because the technology
is evolving so quickly,
we are busy fine tuning our tools.
But we do want to, first of all,
help our partners, our ecosystem.
Amazon has Fulfillment by Amazon.
We will do something similar to
benefit our partners who are in our
ecosystem.
But why not?
I think, probably,
we'll have the best big model for
E-commerce.
We have so much rich data and
then our training has been taken
into all the different successful
history.
I think,
we are thinking about that, but
not immediately [INAUDIBLE].
>> Speaker 1: That's great.
So in the meanwhile, can you tell
people in companies that would like
to get that kind of capability, but
they have to develop it themselves.
What are the top three lessons from
your experience for
other large companies?
>> Speaker 2: So, as we mentioned
earlier, I think, first of all,
team, people.
I think,
if you don't have the right people,
you cannot get in stock, right?
And secondly, the leadership.
The leadership have to embrace this
change.
And then, not only just embrace it,
but also try to facilitate the
hiring of these people, give them
high salary, reward them properly.
Because, as you know,
people who know this now, they can
easily find a job in the Bay Area
with the package better than
Stanford Professor, right?
So we have to kind of compete for
these people.
So, talents, leadership and then,
I think,
the kind of coordination among
different units of the company.
It's never a kind of a single
action from a particular unit.
You have to get every unit within
your company
to be on the same page.
That's what I said about the third
thing, that,
you have to have coordination
among different units to hire
the right people to work with them.
Not say, this is this AI guy belong
to the sales team,
I don't want to work with them, I'm
the business side, business team.
That will hinder the development of
the AI technology in your company.
>> Speaker 1: That's great.
Thank you very much for
a fascinating presentation.
>> Speaker 2: Thank you.
>> Speaker 1: And we conclude,
what I'd like to do is,
share a quick preview of the next
event in our speaker series.
On June 27th,
we are going to host Joe McMorrow,
who is the Vice President of Supply
Chains Transformation at Cisco.
As many of you know, Cisco is
a global technology leader.
In this session, Joe will discuss
how Cisco is leveraging AI across
its global supply chain.
He will highlight key use cases and
lessons learned.
Joe will also share his vision for
what's next in the company's AI
evolution.
We look forward to seeing you in
this upcoming session.
And now,
I'll hand it back to Barchi for
a few final remarks.
>> Speaker 3: Thank you Haim.
And many thanks to Professor Shen
and to Dr.
Qi, for a fascinating discussion.
As I mentioned earlier, we ask
that you please take a moment to
complete our brief survey.
You can access it easily using the
QR code displayed on the screen.
We also encourage you to use
the link shown on the right to
access the Value Chain Innovation
Initiative website to
learn more about our next event and
to access the recordings of all our
past events.
And with that,
we conclude today's webinar.
Thank you all for joining us.
We hope you have a wonderful rest
of your day and we look forward to
seeing you in future events.
[MUSIC]
