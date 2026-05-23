---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 1aa6f7c8-22e3-4a41-827d-9c241d6a8214
source_title: "Ep73 “The Dangers of Group Think on Decision Making” with Adi Sunderam"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:38:38 UTC
extractor: nlm_bulk_extract.py
---

# Ep73 “The Dangers of Group Think on Decision Making” with Adi Sunderam

## NotebookLM-extracted transcript (Google's ASR + indexing)

(upbeat electronic music)
[JULES VAN BINSBERGEN] Welcome
to the Lauder Institute at the
University of Pennsylvania.
I'm Jules van Binsbergen,
Director of the Institute
and a finance professor
at the Wharton School.
[JONATHAN BERK] And I'm Jonathan
Berk, a finance professor at the
Graduate School of Business
at Stanford University.
This is the All
Else Equal podcast.
(upbeat electronic music)
[JULES VAN BINSBERGEN] Welcome
back, everybody.
Today, we're going to talk
about a topic that I think
is really important for
corporate decision-making
or more generally for
human decision-making,
and it relates very much
to what in statistics is
called Bayesian updating
and the way in which humans
in the decision-making are
able to do that properly
under various circumstances.
So maybe, Jonathan,
first we should spend
some time intuitively
explaining what Bayesian
updating is all about.
[JONATHAN BERK] Yeah, so I
would say Bayesian updating
is when you get new information,
the way you incorporate that
information into what you think
is going to happen in the world.
And it turns out there is one
way of doing that that leads
to the best outcomes, and we
call that Bayesian updating.
And I would say actually that
Bayesian updating is perhaps
one of the least intuitive
branches of mathematics
and one of the most difficult
to understand.
In m-- at least in
my experience,
if I rely on
my intuition,
I'm usually
get it wrong.
I absolutely have to work
the equations out every time.
[JULES VAN BINSBERGEN] No,
I completely agree
with you, Jonathan.
And I think that there are
some very famous examples,
even game show examples,
where the optimal thing to
do according to Bayesian
updating is so counterintuitive.
[JONATHAN BERK] Yeah, so, Jules,
we could talk about the famous
Monty Hall problem.
You're on a game show,
you win a prize if you guess
which door the prize is behind,
and there are three doors.
And so the host says to you,
"Pick a door," you pick a door.
He opens a door that does
not contain the prize,
and you then are asked,
"Do you want to switch?"
[JULES VAN BINSBERGEN] And
one more detail, the door
that's being opened cannot
be the door that you picked.
[JONATHAN BERK] Yes,
it's not the door you picked,
and it's not the door
with the prize.
And so most people look at
this problem naively and
say, "It's still 50/50,
so it doesn't make
any difference."
In fact, you are better
off switching.
The
intuition is as follows.
If the prize is behind the
door you've already picked,
then his choice is 50/50.
It's a random choice which door.
But if the prize is not
behind the door you pick,
then he communicates
information because he's
forced to pick the door
which doesn't have the prize.
And since that event occurs
two thirds of the time
and the event that you're behind
the door occurs one third
of the time, you are best
to use that information.
And that's why you're
better off switching.
But it is very unintuitive,
and you have to work out the
equations to realize this.
[JULES VAN BINSBERGEN] So Bayesian
updating is really hard.
I think a lot of people find
probabilities in general quite
hard to deal with, right?
That is one of the hardest
things in decision-making.
[JONATHAN BERK] And there are
many more examples of how
mistakes people make updating.
But what we're gonna talk
about today, what I think
is interesting about it,
is many of the examples of
the mistakes people made
have difficulty actually
explaining modern behavior.
You know, we see echo chambers.
You know, somebody will believe
that, I don't know, Kennedy was
killed by the CIA, for example,
some crazy notion like that.
And when they get evidence to
the contrary, it makes them more
likely to believe, not less.
And when we see this behavior,
that's really not explained by
the common mistakes people make.
And so the question is,
what explains that behavior?
[JULES VAN BINSBERGEN] No, I,
and Jonathan, actually,
I think one of the solutions
that we need to think about
when you are dealing with
a decision-maker like
this is to actually turn
the question around.
Meaning, if people really
believe that, you should
ask them the question,
"Give me an example of
a piece of information
that if I was able to
give it to you, it would
make you change your mind?"
Rather than trying to give
them a lot of pieces of
information to convince them
that they're wrong about it.
Because once they're willing
to commit to such a piece of
information, it's much easier
to have the debate after.
And, of course,
if the person says,
"There exists no such
piece of information
that would ever make me
change my mind," right,
then we have something
that in Bayesian statistics
we call a dogmatic prior,
which says there exists
no data or no piece of
evidence that would ever
make people move from what
their prior beliefs are.
[JONATHAN BERK] The paper we will
be discussing is called Sharing
Models to Interpret Data,
and Adi co-authored it
with Josh Schwartzstein.
[ADI SUNDERAM] And
I think, Jonathan,
one of the key innovations
of this paper is that the
authors want to consider
the possibility that certain
decision-makers just have what
they call a set of models that
they are unwilling to consider
as potential explanations for
the data that's being presented
to them, and another group of
models that they're much more
likely to relate any piece of
information that they see to,
and see as a confirmation or
try to interpret to the best of
their ability to fit that data
into that set of models that
they are trying to consider.
[JONATHAN BERK] Yeah.
So basically,
for whatever reason,
I always say computational,
you can't think of every
possibility, you make
a subset of possibilities
and assume that nothing
else could happen.
You rule out explanations
of the world a priority,
and then you are
a perfect Bayesian.
Given the explanations
that are available,
you then interpret new data.
And so the problem
with that, of course,
is that if you've left
out the truth as data
comes in confirming
the truth, but you've decided
the truth is impossible,
you're enforced in your
set to give higher and
higher probability to
more and more unlikely
expeditions.
You know, a good example
of this kind of behavior
is the COVID virus.
So, very early on,
it was decided it was
impossible that it could
come from a Chinese lab.
So what that meant was, as the
evidence accumulated, that there
was something very strange about
this virus, you know, that there
was a splice in this virus that
nobody could make any sense of,
you needed more and more
ludicrous explanations of
how, in nature, that splice
could've happened, right?
So we had found out about
pangolins and, you know,
various different creatures,
that somehow or other this
virus got to Wuhan and markets
that people traded the stuff in,
and it became more
and more ludicrous.
But that was a consequence
of you couldn't consider
the likely explanation.
[ADI SUNDERAM] And so
therefore, Jonathan,
I think that this paper,
as much as it is a description
of individual behavior,
I really also like to
interpret it in the context
of sociological behavior.
[JULES VAN BINSBERGEN] In other words,
is it possible that you
grow up in or interact
with a particular group
of people where a set of
explanations are just not
allowed to be considered?
Because if you bring them
forward as hypotheses,
you're ousted from the
group or there are severe
social penalties to that.
And then once you're in that
environment, I think as a group,
you get this collective
assignment of trying to be
super creative in terms of
together coming up with crazier
and crazier explanations.
And I think that some
of the echo chambers,
regardless of which side
of the political spectrum
we're talking about,
that we're currently
seeing on social media,
are actually engaged in
that group activity.
And so I find that it's not just
disturbing in its own right,
but I also think it's a huge
waste of intellectual
resources, 'cause I'm,
I'm not even sure that the
people that are engaging in this
behavior are necessarily people
that aren't particularly smart.
I think really smart people are
particularly good at coming up
with crazier and crazier
explanations just because
other explanations are not
allowed to be considered.
I think so.
So, Jules, l-- why don't
we introduce our guest and
talk about the work that
he's doing on the subject.
So our guest today
is Adi Sundaram, who is the
Willard Prescott Smith Professor
of Corporate Finance at
Harvard Business School.
He's a research associate
in the National Bureau of
Economic Research and currently
also one of the co-editors
of the Journal of Finance.
Adi, welcome to the show.
[ADI SUNDERAM] Thanks
for having me.
[JULES VAN BINSBERGEN] So Adi,
let me start with a
very general question.
What does your model say?
[ADI SUNDERAM] So our model
is trying to think about
how people interpret data.
So, you know,
there's just lots
of news comes out,
like we got a jobs
report today and we
want to know how to
think about what the
jobs report means for the
overall strength of the economy,
and the thing that we do that's
a little bit different than what
others tend to do is people
often assume that, you know,
once the data comes out,
people sort of know
how to interpret it.
Whereas we sort of
say, like, "Well,
let's suppose that
people are open to lots of
different interpretations."
So maybe if I was thinking
about the strength of
the economy, you know,
a low jobs number is actually
fine news because it means
that we are getting a bunch
of automation and, you know,
that's actually going to
drive productivity growth
and it's going to be great.
So we're trying to say that
people are open to, like,
thinking about data in very
different ways, and then
we're trying to understand
the implications for that.
Now, of course,
in a perfectly rational model,
you would do some of this too.
We should be open to a bunch of
different interpretations and
think about what each of those
interpretations implies and
then sort of average over them.
So what we do in our model
that's a little bit different
is just, say, two things.
One, which is not that far
from rationality, is saying,
I like explanations of the
data that sort of fitted well.
I don't like explanations
where you just throw up
your s-- hands and say,
"I don't know," but a
Bayesian would actually
do a little bit of that.
The second,
sort of more
important thing is that
when I'm thinking about
an interpretation that
you, Jonathan, gave me,
I don't necessarily think
about all the other
possible interpretations
you could've given me.
And so I'm sort of
underestimating exactly how
much flexibility you had in
coming up with an explanation
that sort of fits the data well.
That's sort of a very
rough outline of the
model and the paper,
and sort of the key
implication of it really
is that, you know, the truth
need not win in the long run.
Because after the fact,
you can always come up
with a story that sounds
better than the truth.
You know, in our finance-type
setting, you know, you might
say, like, suppose the random
walk hypothesis were true
and stock returns were
really unpredictable.
Well, that doesn't sound
so great when my neighbor
tells me he made a bunch of
money in NVIDIA stock, right?
That just doesn't fit
my data that well,
and therefore I sort of
cast doubt on the random
walk hypothesis for mine.
But it's because the
interpretation was sort
of picked after the fact.
[JONATHAN BERK] So Adi, there are a
whole bunch of reasons for why,
in the end, in the data,
we might observe this
sort of thing, right?
So it could be that it's
just easier to not have all
of these different scenarios
in our heads and it's just
way too complicated to be
a true Bayesian and to have
all of these different models,
and therefore I converge to one.
Another one is, you know,
I was raised in a family and
they've always told me that
particular model that always was
discussed at the dinner table.
There is the possibility that
being surrounded by people in my
social network that share that
reality and everybody confirms
each other in that reality.
What is sort of the prevalent
preference or reason for why
you think people end up modeling
things this way in their head?
[ADI SUNDERAM] Yeah,
you know, I mean,
the place
I would start from is, I'm not
sure we're right, I'll, I'll try
to actually be patient about it.
I'm not sure we're right.
But, you know,
there's two things I
like about this approach.
One is, often,
as you were saying,
we jump to the end,
and it's what,
Kahneman would call
System One thinking.
We just assume that people
are gonna have a gut reaction,
and they're gonna overreact or
under-react, whereas this thing
is taking more seriously,
people actually do spend a
ton of time thinking about data.
This paper has actually caused
me to, like,
read a bunch of the things
that anti-vaxxers say.
It's not like they're
ignoring the data.
They are digging deep, deep,
deep into studies, and
coming up with all, they're
looking at the data,
and so, I am interested
in this idea that,
how can you go astray if you're
really, really data-focused?
[JULES VAN BINSBERGEN] Yeah.
[ADI SUNDERAM] And the
other thing that I think
is just, it's usually
a little bit
outside of our economic models,
but it's like fact
zero of the paper, is that
people spend a lot of time
talking about interpretations.
I mean, I remember this from
the COVID inflation
years v'21 and '22.
After every CPI,
there really was, like,
inflation hawk Twitter
and inflation dove Twitter,
and they would be reading
those CPI reports
in totally different ways.
But interestingly, they'd
always come back
to sticking with their prior.
Like very few of the inflation
doves,
I mean, I will confess,
I was an inflation dove,
and I was wrong.
But very few of the inflation
doves just came out and said,
"We're wrong."
You'd get print
after print of high CPI,
and people would just say,
"Well, it's imputed rents.
Well, it's one-time problems
with goods and services.
It's a one-time,
shipping problem," whatever,
and those explanations
would keep moving around
and keep moving around.
Again, is it exactly that people
like good fits of the data?
There's some psychological
evidence of that,
and other people have run
experiments trying to show that,
there's some evidence of that.
But overall, I think, for me,
what's been fun about this
is just thinking
about why is it that,
when people are really focused
on trying to understand stuff,
they could still go awry?
[JULES VAN BINSBERGEN] I mean,
a more typical,
or a common model of
irrationality would be, say,
something like, "Well, people
just don't Bayesian update."
You're coming at this
from a different angle.
You're saying, "No, no,
they're Bayesian updating.
They're just limiting the set of
possibilities to a small set."
[ADI SUNDERAM] Yes.
[JULES VAN BINSBERGEN] So,
how would you, A,
differentiate those
two models, and B,
do you have any evidence
that in fact your way of
looking at the world better
explains peoples' behavior,
and then C, I assume you do
have some sense of that,
is there any intervention
you could think of
to help with this issue?
[ADI SUNDERAM] Yes.
So, let me do it in parts.
So the first part, I think,
is that one prediction of,
"I have all the models
and making mistakes in
Bayes' rule," if I then
give you a model again,
nothing should happen,
because you already
had that model.
You sort of understood it.
You used it, but you just
used Bayes' rule wrong.
And so there are, like,
quite clever experiments
that do stuff like this.
So, it's like, first I tell you,
"I'm your financial advisor.
The stock will be
worth 100 tomorrow.
What do you believe?"
And then, I tell you,
"I'm your financial advisor.
The stock will be
worth 100 tomorrow,
and here's why."
To do my favorite example,
it's a, you know, like a
technical analysis thing.
"We just hit the head
and shoulders pattern,
and therefore, the stock
will be worth 100 tomorrow."
The latter, in experiments,
is much more effective
than the former.
And so that's a
narrow experimental
view, but, you know,
the nice thing about
experiments is you can
kind of, it's very tightly
controlled, and you can,
like, really say, like,
"The only thing that changed was
that we gave people the model."
So, that's sort of probably
the cleanest evidence.
You know, the evidence in
the world, I would say, is,
there's two types of things.
One is, you know,
and we have some of
this in the paper.
For instance,
if you look at
the beliefs of
people who are
on StockTwits,
which is like, you know,
Twitter for stock market advice,
those things seem to move around
in ways that we would predict.
So, you take someone who's,
like, a bull on Tesla.
Tesla has a negative
earnings announcement.
Going into the
earnings announcement,
the bulls were saying,
"Just wait for this
earnings announcement.
It's gonna be great,
and it's gonna take
Tesla to the moon."
After the earnings announcement,
the bulls get disappointed for
a few hours, but eventually
they coalesce on, you know,
some explanation, like,
"Elon Musk is a genius.
He's gonna figure
it out eventually."
This was a, you know,
just like the CPI thing.
There's like,
"We're gonna come up
with some reason that
explains away this piece
of data that doesn't sort
of fit with the world view."
And you see that not only
in financial settings.
There's also a bit of
evidence that you see stuff
like this for policy views.
So, you know,
there are some papers that look
at things, like, what are people
saying in the aftermath of,
like, a school shooting
or something, and it's like,
people become a little bit
more open to gun control
for a few days,
but then they go back.
And, you know, more broadly,
I think, for a while at least,
there was this real puzzle in
sort of political science that
the polls seem quite volatile
in the short run,
but quite sticky
in the long run.
So, you know, like,
there's news that
a politician does
something terrible,
the polls will move,
but they'll only move
for a week or two,
and then they'll sort of
go back to where
they were before.
So, all of those things,
I think, are sort of
consistent with our model.
The other one, you know,
that we've been talking
about a little bit is,
like, conspiracy theories,
like, people linking facts
that are just very,
from a sort of semi-objective,
you know, it's not
really objective,
but, like, facts that you
would be surprised
to be linked together.
That comes out very
naturally in this view.
It's just a prediction of
the view because linking
stuff together tends to
make it less surprising.
You know, saying that A
and B are highly correlated,
that just means that actually,
the only surprise was that
A happened,
and wasn't a sort of independent
surprise that B happened.
So those are, I think,
the types of things that
point in this direction
in the data, but again,
it's work in progress.
I mean, we're still trying
to figure it out, really.
[JULES VAN BINSBERGEN] Well,
I want you to get to the
third part of my question,
but before you get there,
just the intuition, and
correct me again if I'm wrong,
but the intuition, though,
is something like this.
An event occurs because the
person has a closed set of
possibilities about the world,
what you would call models.
The most likely model, given
that event, is not in their set,
so then they have to look within
their set for an explanation.
They get forced to do that.
They're Bayesians, right?
[ADI SUNDERAM] Yup.
[JULES VAN BINSBERGEN] So, what
they then say is,
a very unlikely event
has occurred
because that's
the only possibility, right?
And then they will
say, well,
and so that explains just some
unlikely event
that a full Bayesian
would look and say,
"No, no, no, there's a much
more likely explanation,
it's just you haven't
thought about it."
That's the essence.
[ADI SUNDERAM] That's
the essence, yeah.
[JULES VAN BINSBERGEN] Yeah,
although, Adi,
from what I heard
you say earlier, I think
to some extent,
you can also model this
as that people are willing to
to really morph the data
observation into a different
data observation, right?
[JONATHAN BERK] If
you're saying, yeah,
the inflation number was high,
but the inflation number wasn't
really the inflation number,
it was just something else
that made that observation
have noise in it, or therefore
I don't have to take the data
point as seriously as I usually
would have, because I'm just
saying there's something wrong
with the data in some sense.
Those two are isomorphic,
aren't they?
[ADI SUNDERAM] Yeah.
And so the key thing, like,
sort of in connecting your
two comments is that in the
set of things you're willing to
consider is that interpretation.
So if I stipulated that you
cannot use the explanation
that the system is rigged
or, you know, whatever,
then you can't do this morphing.
But people are very open
to the interpretation that
actually the data is just
messed up for whatever reason,
and that's what sort of
gets this off the ground.
And just one more point on,
on what Jonathan said is
even if the true model is
in the data, so you know,
even if I consider the
possibility that stocks are a
random walk and unpredictable,
because I'm not sort of
putting the right weights
on these things ex-ante,
I'm going to find ex-post
very compelling that, like,
my neighbor must be a genius
because he figured out that
NVIDIA was going to go up a lot.
[JONATHAN BERK] I can
give you an analogy.
As you know, I like to ski,
and there, I can remember an
incident in very deep powder,
where what happens is you fall
And you can lose a ski
because it's buried in
the powder, right?
So now you have to
search for the skis,
and if you search for like
half an hour and in a half
an hour you're searching in
all the obvious places and
there's no ski, and then I,
at that point, turned round
and said, "Look, by definition
this ski has to be in a,
a low probability place
because we've checked the
high probability place.
So now let's look at all
the-- It's all going to be
a crazy explanation, it has
to be one of those," right?
And so then we did that
And we found it in
a low-probability place.
What I think you're saying
is, repeat that whole thing,
but let's say I only look in
half of the high probability
[ADI SUNDERAM] Yeah, exactly.
[JONATHAN BERK] And I've checked all
high, the other half, I ignore
the other high probability,
I'm still going to, at that
point say, it has to be in
a low probability place and
then start searching in the
low probability place, right?
[ADI SUNDERAM] Yes.
[JONATHAN BERK] It's just that I
made the mistake of not checking
some high probability places.
[ADI SUNDERAM] Exactly.
[JONATHAN BERK] So again,
so let's go to Part C
of the problem, which is,
obviously, it's suboptimal for
you if people behave this way.
Are there any particular
interventions people could do
to not engage in this behavior?
And let me
preface this by saying,
Bayesian updating is hugely
computationally intensive,
so most of us don't
actually do it, I'm sure.
We have some rule of
thumb to make it simpler
and one rule of thumb is
don't consider everything.
So that's not a, I don't want
you to say to me, "Jonathan,
we just have to tell people
to consider everything."
[ADI SUNDERAM] No, I mean,
but I think, you know,
You, your intuition is like,
how can we get heuristics
that are closer to Bayesian
updating but sort of satisfy
the computational constraint
or whatever, and you sort of
develop these things over time.
So for instance,
academics in finance and
people who work at quant
hedge funds and things are
pretty familiar with the notion
that the model can be overfit.
They know that,
and it's not that
every time you see a
beautiful t-statistic
of two for a trading
strategy, you, like,
go and do the full
Bayesian whatever.
You just know that you're
supposed to be a little bit
skeptical of that because
it's likely overfit.
And so I think bringing that
intuition into other settings
can be helpful, you know?
I mean, I think the basic
questions you want to ask
yourself are things like,
"Would I have found
this explanation
at all possible,
like, before the CPI print
came out?
Would that have entered
my mind as a thing that
I would even remotely be
willing to entertain?"
Those kind of things,
at some level,
again, it's a little bit hard,
but, like, I mean, again,
I was an inflation dove.
I sort of knew even in the
moment that I was indulging in
some ex-post rationalization.
[JULES VAN BINSBERGEN] I think
you're a huge exception,
and the reason why I think
you're a huge exception is that
one thing that I
always find very curious
about being a professor and
also about students is that
the moment that a student
or a professor understands
something, you cannot imagine
a world anymore where you
have not understood it,
and you immediately re-update
backwards this, as if you've
always understood this.
And the best way in which we
see this is that we immediately
find everybody who doesn't
understand this an idiot,
even though five minutes ago,
we were part of that group.
And yet, we are in no way
willing to admit that.
So I'm worried that when
you're saying, you know,
"Let me go back and see
whether I would ever have
entertained that," I think that
once people are entertaining it,
it's very hard to put themselves
in the position of a person
who didn't entertain that.
And secondly, you know, I,
I like the micro decision
maker point of view,
but maybe we can broaden
also the discussion to say
within a firm we have a larger
organization with a lot of
different decision makers.
And by the way,
I think the phenomena that
you describe happens
all the time, right?
We have a medical company,
we make it very clear that we
have staged investment processes
where we beforehand say,
"If this benchmark isn't hit,
then we should definitely
do this or that."
Then the benchmark isn't hit,
and then everybody comes
up with a reason for why.
The reason why we didn't
hit the benchmark didn't
really have anything to
do with the fact that our
company's just not doing well.
We attribute it to
some external force,
we reinterpret the
data and we continue
with our investment.
And obviously,
this can really
destroy a lot of
value for companies,
and I think it does all
the time because people
are so stubborn in sticking
with the belief systems that
they collectively have.
So as an organization,
do you think that there
are institutions that you
can put into place to try to
avoid these sorts of pitfalls?
[ADI SUNDERAM] It's
a great question,
we're thinking about it.
Let me give you one example
where I think things sort of
work well given the objective.
So criminal justice, you know,
the way we set up the
justice system is there's
prosecution and defense.
They both see all the data
and then they make arguments.
In our sort of view,
that gets you the
place where, like,
a lot of the data's
thrown out because
the prosecution has
a good story for it,
the defense has a
good story for it.
You can't really use it
to convict or not convict.
But if your objective is
to convict only in the
cases where, you know,
you're guilty beyond
a reasonable doubt,
if your standard is, like, we
want unambiguous certainty that
there's really no interpretation
where you didn't do the crime--
[JULES VAN BINSBERGEN] Yep.
[ADI SUNDERAM] Then
setting things up in the
prosecution defense way is
the, is a way to implement that.
Like, the only things that we're
going to get are like you were
literally caught red-handed,
that's when you get convicted.
[JULES VAN BINSBERGEN] Understood.
[ADI SUNDERAM] So
that's different than
a business setting,
but that's a setting
where actually, you know,
the idea that we're all
going to see the data first
And then we're going
to make arguments,
I think sort of makes sense.
In your organizational setting,
I mean, I think the one thing
we've sort of thought about
and experimented with is
rather than setting things up
as prosecution defense where
there's sort of, you know,
one team is for it and one
team's against it, try to set
up teams that are model driven.
So if you took the sort of
sports example, you don't want
people switching back and forth
between the Moneyball argument
and the, like, old-fashioned
baseball scout argument for
why we should hire a player.
Instead,
what you want is you tell
the Moneyball people,
"You go off by yourselves
and come back with what you
think is right for each player."
You tell the scouts,
"Go off by yourself
and come up what you
think is right for each player,"
and then you need
to integrate across them.
So actually separating teams
into sort of model-based views
and then having a judgment
maker who looks at their
models or interpretations
separately gets you closer.
Again, you know,
basically what we're
trying to do is get to
what the Bayesian would do.
Like, get to,
"I want to hear all the
models and then I want to
sort of have a view on how
ex-anti-likely they were, plus
how well they fit the data."
So again, this is not perfect,
it won't get you all the way
there, but sort of organizing
things in, "I want to group
people by their view of the
world," as opposed to, "I want
to group people by the outcome."
That might be able to help,
but that's a question
we're, like, working on
pretty actively actually.
[JULES VAN BINSBERGEN] One last
question, which is,
I know you have views
on social media and this
phenomena, so what do you think?
[ADI SUNDERAM] So one,
this phenomenon's not
exclusive to social media.
Like, people persuade each other
at the water cooler, at work,
people exchange interpretations
all over the place, you know,
in our, in our academic thing,
you know, it's if somebody
surprisingly doesn't get tenure
at a top school, you will all
make up reasons that you think
that happened, right?
What I think social media
does is it really amplifies
the ability for people to
get into these, like,
very segmented communities.
And so, you know,
prior to Twitter,
would all of the inflation
doves been talking to each
other and all trying to figure
out why the latest CPI release
was, why we should ignore it?
No.
And so, you know,
social media, I think,
really amplifies these things.
If I just talked to my
neighbor or something,
I wouldn't have gotten
such a precisely, you know,
optimized narrative.
But, you know, I mean,
I think the other thing
about this is that, again,
in the rules of thumb type
or heuristic type argument,
over time people will get better
at using social media and, like,
not really overreacting to
one person's interpretation.
But because it's sort
of still a new thing,
I think we're still at
the stage where, like,
those heuristics and sort of
rules of thumb and, you know,
even social guard rails
don't really exist yet.
[JULES VAN BINSBERGEN] So I think that
social media is very
special in the following way.
People are generally bad at
understanding selection effects.
And so in this particular case,
the information that you're
fed and the opinions that
you hear from others, and
they're so carefully selected
to already coincide with your
own, that you're going to have
your own beliefs confirmed,
then you attach value to that.
And so as a Bayesian updater,
if you knew that those people
had been pre-selected to only
agree with you from a huge
set of people with opinions
that potentially could not
agree with you, you should
not put any weight on those
additional opinions because
they're not representative at
all for the cross-sectional
distribution of opinions.
But now if you overweight that,
you just get further and
further confirmed.
So I think that pre-selecting
these audiences that way, even
for a perfectly Bayesian updater
who just doesn't understand the
selection effect, is already
disastrous, wouldn't you say?
[ADI SUNDERAM] Yes.
There's a version of that that
is about interpretations and
then, you know, that people make
this argument more generally
that social media is a bit of
an echo chamber and that, like,
you're actually not even
seeing the information.
Like, if there's
a bad CPI print,
do the inflation
doves even know about it?
Both things seem to happen.
I think, you know, actually
Matt Gentzkow and others have
some interesting work suggesting
that the informational type of
echo chamber is not quite as
strong as one might worry about.
So, you know, even, like,
people who watch Fox News
basically know the set
of news results that
everyone else knows.
It's not like we're missing
huge swaths of the data or
the information per se,
but you're getting a bunch of
different interpretations of
that data than you would on,
you know, MSNBC or something.
But, you know, in our thing,
I think the difference is in an
information-type driven world,
the second I drop one bit
of information on you,
like the vaccine has
been pretty effective,
everybody immediately agrees
that vaccines are now good.
Whereas in our world, you know,
if I drop that bit of news
on you, you make up a bunch
of stories about how the
studies were run poorly and
the academics are corrupt
and this, that and the other.
And so at some level, this
sort of interpretation-based
echo chamber is sadly, I think,
more robust than an
information version.
[JULES VAN BINSBERGEN] Wonderful.
Well, Adi, it was
very interesting discussion.
I mean, these are the big
questions of our time.
I think it's hugely influential.
So it was really interesting.
[ADI SUNDERAM] Yeah,
thanks a lot.
This was really fun
And like I said, I mean,
I want to be cognizant
that I don't think we have
fully figured it out yet.
I might be wrong, but it's
certainly, like you said,
it's an important and
very interesting set of
issues to think about.
[JULES VAN BINSBERGEN] Well, Adi,
if I hear any other
interpretation of
what's going on,
I will ignore it
because I really like
what you just proposed.
[ADI SUNDERAM] Very good.
[JULES VAN BINSBERGEN] Thanks for listening
to All Else Equal podcast.
Please leave us a review
at Apple Podcasts.
We love to hear
from our listeners.
And be sure to catch our
next episode by subscribing
or following the show wherever
you listen to your podcasts.
For more information
and episodes,
visit allelseequalpodcast.com
or follow us on LinkedIn.
The All Else Equal podcast
is a joint production of
the Lauder Institute at the
University of Pennsylvania and
the Graduate School of Business
at Stanford University, and is
produced by University FM.
(upbeat electronic music)
