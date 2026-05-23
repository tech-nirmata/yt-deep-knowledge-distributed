---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: c5ef9bf0-827c-4853-9fc9-7caac4254240
source_title: "Deep Learning in Economics II"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:35:29 UTC
extractor: nlm_bulk_extract.py
---

# Deep Learning in Economics II

## NotebookLM-extracted transcript (Google's ASR + indexing)

All right, I think we will
go ahead and get started again.
So before lunch we were talking
about stuff that, you know, tools
that come almost entirely from
the machine learning literature.
So I tried to show you economic
applications of them.
But if you want to go back,
understand those tools,
do some of the original readings,
you know, you'll be reading things
in machine learning proceedings.
And now I want to shift gears and
assume that, you know,
we've mastered whatever machine
learning we know to be able to
extract our structured information
from our unstructured data, so
from our text or images.
And now we're ready to do our usual
economic stuff with them.
But, you know,
having extracted them,
we understand that what we have is
not, you know,
the truth in some sense,
that it's measured with air.
You know, probably even the best
deep neural network model is going
to make some mistakes.
And we want to take
that seriously or we want to know,
do we need to take that seriously?
And the answer is going to be yes.
And so I'm going to shift now to
talking about econometrics and
I will talk a little bit
about some work that's been done in
the statistics literature.
But by and large,
kind of the punchline of the next
discussion is going to be that
actually econometric tools that
we've actually had since the 1970s,
we can take those and
we can apply those to predictions
from deep neural networks.
And there's some things to
kind of to be aware of.
But basically our traditional
econometric methods work
in order to ensure unbiased,
robust, efficient inference
with unstructured data.
All right, and
so this talk that I'm going to be
giving over the next few minutes is
based on work with Jake Carlson.
Jake is a Ph.D. student at Harvard.
He's an econometrician,
a really fantastic econometrician.
He's only going into his fourth
year, so he won't be on the job
market for a while, but he's
definitely someone to watch for.
All right, so
to kind of step back and recap our
motivation from this earlier today,
stated slightly differently.
So we want to use unstructured data
in our research.
We can't use it directly.
It's high dimensional,
it's complex, we can't interpret it
in its raw form.
And so instead our goal is to
extract low dimensional information
from that unstructured data.
And kind of in the language of
machine learning, this is referred
to as structured data.
And structured
data is low dimensional.
It's interpretable,
we can take it and we can plug it
into whatever statistical
Analysis that we want to run.
And so there's a really,
really long history of using
unstructured data and economics.
And so if you think about
things like institutions, I mean,
polity uses text in part to measure
institutions, kind of any conflict
data set, most of those are based
on newspaper and other texts.
Political stability, policy,
uncertainty, violence, all of these
are extracted from text.
Economists have been studying these
things for a long time, long before
there was deep learning.
We also try to derive things like
sentiment or topics or
other structured features from
government transcripts,
from corporate filings,
earnings calls, patents, web texts.
Satellite imagery is used to
measure economic activity,
economic development, urbanization,
particularly in places where we
don't have a lot of great
higher frequency economic data and
remote sensing data supplements,
sparse ground measurements of
temperature, precipitation,
pollution, agricultural land use,
illicit activities,
deforestation, the list goes on.
And so in short, using unstructured
data and in economic
analyses is not a new thing.
But what is new is traditionally
it would be really costly to
extract structured information
from these data sets.
And so typically it was some
large scale external initiative
that extracted the data.
So you have like
preo conflict data.
They don't really
share their methodology.
Somehow they extract conflict
from newspaper articles.
We don't know how they do it.
It's probably humans reading the
article, but we don't know exactly.
And that's just what there is.
You know, if you wanted to use that
information, you use the data sets
that are typically
kind of constructed by some
large scale external initiative.
But advances in computing and
deep learning have drastically
reduced the cost of being able to
extract structured information
from text and images at scale.
And so it's become super common for
economists actually to create
our own data sets.
So start with our own 100 million
newspaper articles and extract our
own information from those.
And economists
have done this in different ways.
You know, traditionally we might
have looked for
certain keywords, and by the way,
everything I'm going to say today
applies to that technology as well.
But deep neural networks
are the state of the art tool for
large scale features extraction
from unstructured data.
And we kind of typically assume
that if you're doing research
today and you're trying to extract
information from text or
from images, you're probably going
to be using a deep neural network,
or at least maybe you should be.
All right, so neural networks will
not generically produce unbiased
predictions in finite samples.
And the measurement error that
comes out of a neural network,
there's really no
conceivable scenario under which we
would expect that measurement error
to be Classical.
So you have to make choices as
the researcher about what type of
neural network architecture you're
going to use, the distribution of
your training data,
what type of data is that neural
network going to see.
You have to make lots of
implementation details about your
hyperparameters, and all of those
can introduce systematic biases.
Even leaving all of that aside,
the fact that we have nonlinear
transformation at each layer
of the neural network, and
the frequent application of neural
networks to binary or
multi class classification,
that alone violates the assumptions
that are required to have classical
measurement error.
And so basically,
if there's measurement error in our
neural network, there's kind of no
reason why we would be able to
assume that it's classical and
that we can just ignore it.
And any biases and
the predictions that
you make with a neural network,
sort of in your first step of your
estimation, where you're predicting
your structured data, any of those
biases will propagate to estimators
that rely on those predictions.
And that's going to affect both
your point estimates as well as
uncertainty quantification.
So if you have a large data set,
sampling variation is likely to be
very small.
But if you have a poorly performing
first step predictor, so
in other words,
if the neural network that you're
using to predict your structure of
data in the first step, if that's
not very good, that can introduce
an enormous amount of uncertainty
if you take that into account.
And so really if you ignore that,
you're going to make very confident
predictions.
But if you take into account
that your neural network is
not making very good predictions,
there's actually going to be
an enormous amount of uncertainty
about what we can actually learn
from that data that you extracted.
And I'd say that concerns
about imputation bias from neural
networks, so bias from imputing
that structured data are further
heightened by, by the availability
of off the shelf neural networks
that are very cheap to implement.
And so you could easily say, okay,
I'm going to make predictions with
GPT4.
400 and mini, with Claude, with
another version of GPT, with Gemini
2.0 Pro and the list goes on.
There's so
many different off the shelf neural
networks that you can just use and
that raises concerns that people
might go and p hack with that.
I'm going to see what it looks like
with gemini and with 400 mini and
I'm going to choose the one I
like best.
And hopefully nobody's doing that.
But we don't want to have to
assume good intentions.
We want a way to be able to take
kind of that bias seriously so
that once you correct your standard
errors and your point estimates for
the bias in your predictions,
you know, GPT and Gemini will give
you the same answer.
>> Speaker 2: The neural network is
developing a model for
data in order to reduce its
dimensions down to this lower
dimensional representation.
So if they then take an economic
model and
estimate it with the data generated
by the neural network is sort of,
I may just be testing whether my
economic model represents the model
of the neural network very well
rather than the sort of model
of the data from which yeah,
in some sense the neural network
is just a form of the model.
And so in some sense, if literally
using a log linear model, and
I estimate a log linear model,
then that's going to provide
a good fit to the neural network,
but might not represent the neural
unstructured data.
>> Speaker 1: Yeah, absolutely.
Yeah, that's a great point.
I completely agree.
All right, and so in short,
hopefully we're on the same page.
I will say I think right now neural
networks are the new hot thing.
There is a rush to
get out papers and I mean there's
a lot of papers where people like,
shockingly enough, there's not even
any test set, like nothing.
Forget trying to correct the bias.
We don't even know how
well this thing is doing.
And you know,
so part of what I want to do is
just to convey like, you know,
we have to take this seriously.
And as I mentioned this morning,
Sendhil Ashesh, other co authors of
theirs also have done a lot of
great work showing that
we can't assume that these models
are going to be accurate.
Humans are really bad economists,
maybe even are really bad at
predicting when they're going to
work well and when they're not.
And you know, so
absolutely we need a test set to
see how the models are doing.
But we're going to take that a step
further now and say, you know,
not just should you have a test
set, you know,
to see how well we're doing.
Because we could sit here and
Argue all day,
you have a classification problem.
The F1 is 0.8.
You know, F1 is a harmonic mean
between recall and
precision that's used to evaluate
classification models.
We could sit here and
argue all day,
is that good enough or not?
There's not an answer to that
question unless we take into
account in a principled way
how that bias propagates into
the estimates that we want to use
those predictions for.
You know, a related point
is if you're not very happy with
your neural network predictions,
there's investments that you can
make to make them better.
So, for instance,
you could train a larger model,
which will be kind of more finicky,
to train, more costly to run, but
it will work better.
You could collect more training
data, you could collect higher
quality training data.
You could just train for
longer on that additional data.
You could keep refining your
implementation details.
These are all investments that
we can make, but they're costly.
And so how do I know
how good is good enough?
And the answer to that question
is going to depend on how the bias
from my imperfect neural network
propagates to point estimates and
uncertainty quantification and
whatever I ultimately care
about estimating.
You know, so here, you know,
we're taking the perspective.
What you care about at the end of
the day is not how accurate your
neural network is.
What you care about at the end of
the day is, you know, some quantity
of interest, an economic
quantity of interest that you're
trying to estimate with the data.
And so we want to be able to
actually quantify how that bias
propagates so we can know, is this
good enough or do I need to keep on
making more costly investments?
You know, sitting there all day
labeling data when my RA won't do
a good job of it, or whatever
those costly investments might be.
Not talking
personally about anybody, but.
All right, and so in order to
address these challenges, Jake and
I developed a framework that
we call mars, which stands for
Missing at Random Structured Data.
And MARS provides a framework that
we can use to conduct valid,
efficient and robust inference.
And I'll talk about what we mean by
all of those terms in a little bit
on estimates that incorporate
unstructured data through their low
dimensional features, which is
a fancy way to say we're going to
use unstructured data in our
analyses, we can't use it directly.
And so first of all,
we're going to impute that low
dimensional structured data,
probably with a neural network.
Although, you know, everything in
this framework would apply to kind
of other ways of imputing that as
well, and so we're going to frame,
as the name suggests,
inference with unstructured data as
a missing data problem because our
raw unstructured data set typically
lack the low dimensional summaries
that are relevant for our analyses.
So I think I gave
the example this morning.
We want to know if this newspaper
article talks about economic
policy uncertainty.
But the author didn't start
the article by saying this talks
about economic policy uncertainty.
We have to impute that.
And that data is missing because it
would be super costly for
me to go through and
do it all by hand.
I have three 50 million articles.
That's completely infeasible.
We clearly need some kind of
imputation technology
to impute that missing information.
And that technology in
today's world is going to be a deep
transformer based neural network.
And so as the name suggests,
this framework builds upon Rubin's
classic 1976 Missing at Random
mechanism.
So this is essentially taking
missing at random, which by
the way, is also a foundation for
causal inference and applying it
to deep neural networks.
Yes. >> Speaker 2: Are you
thinking of a setup where
ground truth exists?
>> Speaker 1: Yes.
Okay, so you're assuming that
this is a classification problem.
You and I would not disagree what
the classification is.
Exactly.
So there's some ground truth.
We might disagree and that's okay.
But you're willing to take a stand.
So I don't think it's
truth in some deep sense, but
you're willing to take a stand.
That I've measured this.
This is what I mean.
This is what I define as economic
policy uncertain.
This is reasonable.
And I'm going to have, you know,
I'm going to have my validation
data that I'll stand up for.
So I may disagree.
I can think economic policy
uncertainty is something different,
and that's fine.
I think we're not trying to get
truth in some deep sense.
There will be valid inference.
For your definition of economic
policy uncertainty.
If that definition is nonsensical,
then like you've just studied
something nonsensical, but you are
at least willing to take a stand.
This is what I want to extract and
I'm able to extract it.
And I think that's, you know,
I think that perspective is helpful
even for complicated things
like economic policy uncertainty.
I mean, we could argue about what
that exactly means, how it
manifests in newspaper articles.
But kind of, at least once you've
taken a stamp, which by the way,
in that paper they do, they have a
long appendix and they state, this
is exactly our definition of it.
This is how we trained our
RAs to do our audit sample.
Like, you know,
once you take a stand on it,
then at least we can have a debate
and about what it means.
Whereas when people kind of
don't want to take a stand on what
they're trying to measure, then I
think it's harder to make progress.
All right, so
our goal is to take foundational
results from semiparametric
inference with missing data.
And use this to debias
estimators that use predictions
from deep neural networks.
And so the key idea is to collect
a validation sample that contains
ground truth values, which,
as I just said, doesn't have to
be truth in some deep sense.
But you as the researcher
are willing to take a stand.
This is what I'm trying to measure.
And you're able to do that, and
you use this sample to estimate the
bias in the imputed data and then
adjust your estimates accordingly.
All right, and so
I think, you know, I just largely
discussed this, but what do we mean
when we say ground truth, not truth
in some deep sense, which may
be unattainable, you know, for some
of the things we want to measure,
but rather ground truth is obtained
through some costly process?
You know, typically that would be
in annotation by a highly skilled
and motivated human expert.
You know, in the remote sensing
world it might be ground station
data, which is where the term
ground truth comes from.
You know, in some contexts we might
think it's a very expensive,
you know, neural network and
you believe that's going to give
you the truth.
But even in that case,
typically it would be good to have
a human back that up.
And so neural networks, from
an econometric standpoint, they're
going to be treated as a black box.
I mean, we have no way to
characterize, you know, say, the
convergence rate of a transformer.
That's just well beyond kind of
what we can do because this is such
a complicated object.
So really to make, you know,
some people are thinking about, you
know, characterizing simple, you
know, two layer neural networks or
whatnot, but it's very complicated.
You know, we're not going to make
progress at this point in time
given the state of our knowledge
and, you know, characterizing,
you know, formally a transformer.
So we want to treat it as a black
box and we're going to treat it as
a black box, but it's not
a complete black box because
the outputs that come out of that
transformer neural network have to
be interpretable because you have a
clear, implementable procedure for
measuring what you want to extract
for measuring your ground truth.
And so that's what ground
truth means.
I can hate your definition of it,
but you have a coherent definition
that can be applied and then
you can have valid estimates for
what you are trying to measure.
>> Speaker 2: Yes, the validation
sample should be
different from any training sample.
>> Speaker 1: Yes. >> Speaker 2: In
the sense that it's completely
separate, it's not being fed into
the machine learning model.
>> Speaker 1: So the otherwise kind
of exactly yeah, exactly.
And so what you do is, you know,
you have labeled data and
then you're going to do sample
splitting.
Yeah. And you don't use that.
You don't use that data to train.
You don't use it also in your
kind of inference
sample to compute your estimates.
This is data held apart that's used
just for correcting for the bias.
And the key thing is that this
validation sample must meet
the missing at random assumption,
which says that
after adjusting for anything,
you can observe annotated data.
So the data you've labeled and
unannotated data,
the data that you haven't labeled,
should be comparable in their
ground truth values.
And so this is basically saying
you have your labeled data
conditional on observables is
a representative sample.
And this parallels the selection on
observables assumption and
causal inference.
Causal inference is a missing data
problem because you're missing
control observations for
treatment and vice versa.
And so basically everything we
do is going to parallel causal
inference, which I think is nice
because it makes it more intuitive.
But in short,
you need a representative sample of
labeled data.
And why, like,
why is this so important?
I mean, it's so
important we name the framework
name missing at Random after Ruben,
who also named it that because
it's very important.
And so if you do not have
a representative sample of ground
truth data after you adjust for
observables, if you have a non
representative sample,
you just have no information
to correct sort of the biases in
your unlabeled data that don't look
like your label data because you
don't have kind of,
you don't have representative data.
And so you'd have
to make assumptions, right?
You'd have to assume, well,
the bias of this neural network and
my label data looks the same
as the bias in my unlabeled data.
And you really don't want to do
that in the case of neural networks
because there's a huge literature
showing that that assumption is
usually not going to be valid.
For instance, maybe you don't have
labeled data for a subset
of observations because it's very
difficult to get data for them.
Well, your model's going to be
trained on data that looks like
data that's easy to get, and so
we'd expect it.
And there's a huge literature
that shows that it would do worse
on that data that looks very
different from its training data
that's difficult to get.
So in short, I think economists,
sometimes we're just comfortable
making assumptions like this, and
maybe sometimes
it really is the best you can do.
But we really don't want to
make strong assumptions
on the form of the bias from
the neural network because we
cannot characterize that.
It's too complicated of an object.
And we have plenty of reason
to think
that this bias is very complicated.
And so we'd rather just have
a representative sample and
be able to measure and
avoid those assumptions.
And by the way,
in a world where researchers
are increasingly creating their own
data sets from text and
from images, this is quite feasible
because you're the one who's
choosing how to annotate data.
And it doesn't have to
be completely random.
You know, it can be based on,
you know, based on observable,
stratified sampling.
And we'll talk more about, you
know, how you collect this data and
things like unbalanced data sets.
But in short, this assumption is
feasible in a world where you are
the one putting together the data.
Okay, I think I
kind of largely went over this,
but there are some situations where
the entire reason why you want
to use a neural network is that you
have no ground truth, and
you cannot have ground truth for
some subset of observations.
And so imagine, you know,
you want to predict famine in
a conflict zone.
There's no way to get on the ground
to collect ground measurements.
And so you're going to use
satellite data, and
there's just no ground truth,
because that's the entire reason
why you're using satellite data.
And people have thought about
this problem in general.
You just have to assume that
the form of the bias is the same
as the sample for
which you have ground truth data.
There's a big remote
sensing literature that says not to
do that, by the way.
But sometimes it is the best
that you can do.
And I think you just have to own,
like, okay, this is a proxy.
I don't really know what crop
output in South Sudan looks like.
But, hey,
we need to predict whether there's
going to be a famine, and
this is the best we can do.
It's an important question.
And so I'm going to proxy, and
I have no problem with that.
Like, if you don't have ground
truth data and you can't have
ground truth data, and you say,
okay, well, like, this is a proxy,
then that's, you know, that's.
I think that that's fine,
because then at least we're having
kind of a honest
conversation that I don't know
what the bias in this thing is.
I'm not treating it as the truth.
But if you want to treat it as
the truth, I would encourage having
that kind of that representative
ground truth data.
And so Mars directly addresses this
kind of fundamental limitation of
neural networks, which is that they
have this bias that shifts in
complex ways with the training data
and how that interacts with what.
You're feeding into it and
is too complicated to characterize.
We're addressing that limitation
by having a representative sample
of how the neural network is
performing.
All right?
And so there's an entire literature
on debiasing with a ground
truth annotation sample.
So there's been a big literature
in statistics,
mostly under the heading of
prediction powered inference.
There's other work.
Agame et al.
Sindel has kind of an applied
framework.
And so I would say that
the contribution of this paper
to this literature is threefold.
So first of all,
we develop a theoretical framework
that unifies this work and links it
back to much older, familiar
problems such as causal inference.
I'd say that the approach in
the statistics literature
is you start with one paper and
that assumes everything that
happens in reality away.
But you have your simple framework,
and then you write another paper
that takes into account this one
complication, and
then you write like a third paper
that takes into account this other
complication, but
it doesn't put them all together.
And I think that's
like a valid way to write papers,
and it's maybe more common.
But in econometrics,
we tend to like the framework that
incorporates everything.
And I think in this case,
it's actually kind of fairly
intelligible to, to people because
it's based on econometrics that
we've been doing for like 50 years.
All right.
And so the second contribution
is to identify estimators that
are both unbiased and efficient.
So the existing literature kind of
overwhelmingly doesn't worry about
efficiency like
we like efficient estimators,
because I feel like economists
are never that well powered.
And so efficiency is very helpful.
And then finally, you know, a
central part of the motivation for
working on this is that there's a
wide variety of settings that come
up in economics that this existing
literature does not address.
And so I just wanted to debias some
of my estimators, and I couldn't do
that because they weren't, you
know, the scenarios that come up a
lot in economics weren't addressed
by this existing literature.
And so our goal is to make it
feasible and easy, you know, for
researchers to apply debiasing
to a wide variety of settings.
I was just sort of wondering.
>> Speaker 2: About the
relationship to
specification searches.
So I guess here you have in mind.
I know the model I want to
estimate, and I want to know,
am I going to get a biased and
efficient estimate of this
particular parameter in this model?
I guess in the background
is potentially also a kind of model
specification search.
Right. So Maybe considering is not
really the right model.
Maybe I kind of overfit in my
training sample.
Another reason for
having an extra set aside to do
the sort of specification testing.
I just wondered
what your thought is on that and
how you see this as being related
to that separate issue.
>> Speaker 1: Yeah, I think that
that's something
that I hadn't really thought about.
But I mean, I think that you're
right that, you know, I guess it
depends if we're talking about
kind of specification search for
the neural network.
Right.
In this case,
it shouldn't matter kind of what
neural network you use.
You should get valid estimates,
unbiased estimates,
if the neural network is really bad
and the confidence intervals will
be really large.
And I'll show you some empirical
examples of this where we try kind
of using different neural networks
to predict the same thing and
some of them are really bad and
then they can range up to
being really good and
like they all kind of, as we would
expect, give the same answer.
But same can be like
huge confidence intervals.
Right. If you've found a model
that's not very good, I mean, if in
terms of how this interacts with,
you know, specification search for
your kind of statistical,
your econometric model that you
want to use the data in.
I mean, I haven't really
thought about that.
So in everything I do today,
we're going to assume that if you
hadn't imputed the data, you know,
if you hadn't imputed that data
with a neural network,
if you just had the ground truth,
structured data, then your
estimates would be identified.
So we're ignoring any other
of the myriad of complications that
come up with identification to
just focus on this one problem.
You would have identification
if you had your definition of
the ground truth, but
you don't have that.
You're imputing that.
And so we're just focusing
along that single dimension.
All right, all right.
So, you know,
from a theoretical perspective,
we provide a framework that unifies
recent literature on doing
inference with black box AI models.
So when I say black box,
I mean we're just going to, we're
not going to try to characterize
anything about the transformer
because we basically can't.
And so we're going to integrate
that literature, which was largely
developed across disciplines that
don't really talk to each other and
it doesn't really
cite each other by and
large, especially not at first.
And then we're going to integrate
that with some older literatures.
So first of all,
there's an econometrics literature
on measurement error which is
probably the most closely related
to what we're doing,
because this is ultimately
a measurement error problem.
It's a measurement error created by
this complicated thing,
the neural network.
But at the end of the day it's
a measurement error problem.
We're going to
relate this as well to widely used
inference methods that incorporate
machine learning based first steps.
So the Debias machine learning,
basically you can show that our
framework is equivalent to Debias
machine learning, but in Debias
machine learning they're just,
they're solving a very different
type of problem.
And then finally two classical
literatures on missing data and
causal inference.
And so it's kind of interesting.
I was talking a bit to
Whitney Newey about this and
he said, like Robbins,
who's one of the main guys who did
this classic literature on missing
data initially he had written
a paper about causal inference and
the statisticians didn't like it.
Like, causal inference isn't
interesting.
This is something that
just biologists do in their
clinical trials.
Not an interesting
statistical problem.
And then so he just
turned it into missing data.
And people thought it was really
interesting because
it's more general.
But we're going to see all those
connections to causal
inference because causal inference
is a missing data problem.
And so in our framework
there's going to be an exact sort
of parallel to what you need for
causal inference.
I think that that's helpful.
I had somebody tell me
we're engaged in a debate at my
university about whether we need to
teach econometrics differently now
that machine learning is here.
Do we need
a totally new econometrics?
And I think, you know,
there's a strong, like,
the answer is no.
I mean, there might be new problems
that we've never thought about,
like, and we have to kind of
think about them.
But at least from the standpoint
of unstructured data, like,
we already know how to think about
this essentially.
And so I think
like that that's a punchline.
All right, okay, so efficiency.
So most of the existing work on
using predictions from black box
AI, they don't talk about
efficiency at all.
You need to take a semi parametric
approach to think about efficiency.
And they don't do that.
One of the papers is like,
this is too complicated.
But we think that economists were
used to semi parametric inference.
And so hopefully I'm not saying
anything that's too complicated for
an estimator to achieve
asymptotic efficiency.
We show that the imputation
of missing
structured data should depend
not only on the unstructured data.
So, like your text or
your images, but also on cost.
Context specific structured
variables that help to estimate
your target parameter.
And so let's say you're going to
use the missing structured data as
your instrument and
you have some controls and
your regression that are not
orthogonal to your instrument.
Like then you would want to use
those controls to help predict
the missing structured data.
This is something called deep and
wide learning, where you use
kind of both the deep learning, but
you incorporate structured data,
you know, so
you don't have to do this, right?
And if you didn't do this,
you did the simple thing, your
estimates would still be unbiased,
but to achieve efficiency you would
want to do that, which I think is
interesting and something that
hasn't been really pointed out.
And then finally, as I said, a key
motivation for this is just to make
it much easier for researchers to
do unbiased inference in practice.
And so we derive robust and
efficient estimators for
descriptive moments,
linear regression
treatment effects identified
through linear IV models, modern
differences in differences and
regression discontinuity.
And so
that's essentially like some of
the most commonly used estimators.
And because we take this semi
parametric approach, it would be
relatively straightforward to
integrate this with recent advances
in an automatic debiasing
work by Chernozhukov et al.
Which then would allow you to
extend this framework to kind of
much more complicated estimators.
All right.
We also handle
a few key extensions.
And so one thing that really
motivated me to think about this
is in economics it's almost always
the case that we're probably not
running our regression at the level
of, of our unstructured data.
And so let's say that we have
50 million newspaper articles, but
our goal is to predict economic
policy uncertainty in the US in
1997 and we're running
the regression at that level.
And so existing work on de biasing,
none of it applies to that problem
because it's all going to assume
that you have ground truth at
the level kind of at which you're
running your downstream regression.
And you know, we could
label all 50 million articles, but
that's not feasible.
Even if we did that, in some sense,
economic policy uncertainty in the
US in 1997 is a population level
quantity and there is no measure of
it in finite samples, right?
At best, we have our kind
of sample of newspaper articles.
You could take a random sample,
but let's say in that paper,
right, they always take the log
of economic policy uncertainty,
they interact it with things.
And so you can't
just do that either.
And so we're going to develop
a framework for using aggregated
structured data that's imputed from
a neural network.
And so you can take all kind of
aggregated and non linearly
transformed predictions and
still do valid inference.
And so that's one extension.
And I'd say, yeah, like 95% of
economics papers, they're always
aggregating the data that they
impute from a neural network before
they actually run their regression.
And so we think this is probably
how the framework
will often be used in practice.
And another kind of, another
extension that we'd like to,
that we look at briefly is suppose
you have some huge data set and the
data of interest is a rare event.
And so, you know,
you have a social media data set,
you only care about, you know,
tweets on pesticides, but
that's going to be a tiny fraction.
And any topic is going to be
a tiny fraction,
almost any topic, maybe politics,
it's the only topic that's not
a small subset of any large kind of
text data that you're using.
And so when we create, you know,
our annotated data,
we need both positive and
negative examples in it.
Right. So how do we do that?
Typically how economists
do that is to use a keyword method.
So we're only going to label
articles about economic
policy uncertainty if they
contain certain keywords.
And the problem with that is like
you no longer, you're violating
like a strong overlap assumption.
Right. You know,
if you're, your population of
interest is all newspaper articles,
you no longer have a representative
label data set because you filter
by a keyword before you label.
And so the statistical literature
would suggest using an important
sampling approach.
And if I have time,
I'll talk about this a little bit.
And so this is all just to say if
you're interested in something
that's effectively a rare event,
there are still valid ways to be
able to label data that will
give you both positive and
negative examples.
All right, okay, so
I want to just briefly relate this
to the existing literature.
You know, I've already
talked about this a bit.
We build kind of most fundamentally
on a much older literature from
statistics and
biostatistics on missing data.
We build on a literature
on semi parametric inference.
There's a literature on black box
debiased AI, it's much more recent.
It doesn't really kind of link back
to this semi parametric or
missing data literature.
So we're going to unite
these literatures and
also treat a variety of additional
common empirical settings that come
up in economics.
I mean, the people by and
large that wrote these papers were
not economists.
And so of course they weren't
interested in our settings.
We relate to
a measurement error literature.
At the end of the day, this is
a measurement error problem.
And this measurement error
literature essentially builds upon
the older missing data literature
to think about measurement error.
We relate to Debias machine
learning and then finally to a huge
literature on causal inference.
And I'll point out some places as
I go through the framework
where there are tie ins
to causal inference.
All right,
so now I want to introduce
the framework,
introduce the notation and
the assumptions that are required
for valid inference.
And so we have unstructured data,
I'm going to call that U.
And we want
that's too high dimensional,
too complicated to use directly.
We're going to impute
the missing structure data M
which is low dimensional data that
we can interpret, that we can use
in our estimating equations.
We observe the structured data
through a process
called annotation.
But annotation
is too costly to scale.
And so we need to be able to impute
missing structured data if we
want to leverage our full sample as
opposed to having to rely on
a really small sample that we
can actually annotate by hand.
And so, and that's, you know,
typically in a big data setting,
that's going to be many orders of
magnitude larger than what we
can annotate by hand.
Right. So there's
a huge benefit to being
able to leverage that full sample.
And in order to do that, we're
going to use a deep neural network.
That deep neural network,
those parameters are not known,
we have to estimate them.
And so we denote that as mu hat.
>> Speaker 2: A very naive
question. >> Speaker 1: Yes.
>> Speaker 2: So naively I'm
thinking, okay, if I have
a manually labeled sample that is
big enough to reliably the bias,
is it also big enough for me to
just get a reliable estimate of the
coefficient I wanted directly from
running on just another sample?
The two must be that if I only did
10 observations, they're probably
too little to both Debias.
And if I consider that
to be my random representation.
I wouldn't get the right estimate.
So in what sense?
Yeah, so I mean,
maybe it's helpful when I actually
kind of show you the expressions.
But like, let's say you have only
labeled 10 things.
You know, your standard errors
are going to be huge.
So you can debias with 10 things,
but the standard errors are going
to depend on how many things you're
debiasing with.
Right? Because you essentially,
like you have the term that you
estimate on your huge sample and
that has, you know, that
has uncertainty associated with it.
If it's a huge sample,
that uncertainty is
going to be very small.
And then you have
term that you estimate, you know,
on your labeled data.
And the uncertainty of
that is going to depend
on how many observations you have.
Although we find in practice that
if, you know, it doesn't
necessarily take a huge number and
you know, in debiasing you're going
to combine kind of those two terms
and if they're really similar,
you then that's fine.
But I mean, I think that
it's an empirical question that we
haven't actually,
we haven't actually looked at.
Although I think in the prediction
powered inference paper that I
mentioned, they do have estimates
that look at that and they find
that your confidence errors get
tighter, although I don't think
they looked at that with kind of
varying degrees of label data.
And yeah, I mean, I do think like
there was, there was also.
I think there's some other work on
this as well, but I don't have that
empirical example of like, when it
becomes like, well, your sample.
So your labeled sample's so large,
there's no benefit to having like
the full data set.
But in principle
we could look at that.
You know, what are the actual
benefits of using the full sample?
It's a good question.
All right, okay.
So we're going to use
a potential outcomes notation,
which is what Ruben used as well,
perhaps not surprisingly.
And so we have M, which
is our missing structured data, and
we have an annotation indicator
which is A and
then M star is our ground truth.
And so if we annotate it, we're
able to observe the ground truth.
And so I want to go through
the assumptions that we need for
valid inference.
So first we need a consistency of
potential outcomes assumption,
which just
says that annotation status
needs to be well defined either
the data is annotated or not.
And that tends to hold trivially.
And the ground truth labels for
any given instance depend only
on its own annotation status and
not on the annotation status of
other instances.
And so this is just basically like
a consistency of potential outcomes
assumption in causal inference.
In causal inference you need
treatment to be well defined and
you need non interference.
That is your treatment status
doesn't depend on
anybody else's treatment status.
And so here it's the same thing.
But think of treatment as being
annotated and you can achieve this
in practice if you have
like a well defined procedure for
annotating data such that
the procedure you apply to
annotate isn't being primed like by
the other, say text or images
that have already been annotated.
All right, the core assumption is
the missing at random assumption.
So after adjusting for observables,
which we denote as X, annotated and
unannotated data are comparable in
their ground truth values.
And so this is analogous to
a selection on observables
assumption and causal inference.
Obviously it will hold trivially if
the data are annotated at random,
but they don't have to be
annotated at random.
Including, you could use some low
dimensional measure from the neural
network like distance and
embedding space to stratify what
data you label.
And that's
fine as long as you have that X.
Okay, the third assumption is that
we have a known and
bounded annotation score function.
So that PI of X is just
the probability that we annotate
any given observation
given observables.
And we need that to be bounded
away from 0 and 1.
And so this embeds what we would
call strong overlap
in causal inference.
And the naming convention that we
use of annotation score function
mimics the usual causal inference
terminology of
a propensity score function.
And so that this thing is known,
we can relax that it doesn't have
to be known.
I'll talk about that in a minute.
Although it's plausible that it's
known if you, the researcher,
are the one annotating data,
because then kind of by definition
it's a known function because
you're the one that's doing it.
The bounded part of it
is important.
And so like if you don't, you know,
if you have zero probability
of annotating certain instances,
that's a violation of the strong
overlap assumption.
We can't know what the bias is for
those instances if you don't
annotate them.
And so
you know, when you talk about
this to kind of econometricians,
like some of them will say,
well wait a minute, you're working
with this high dimensional
neural network and in observational
causal Inference strong overlap
becomes less plausible
as the dimension of the variable
that grants unconfoundedness grows.
But importantly here
U the unstructured data, that's not
what's giving us unconfoundedness.
We have some measure X
that's fairly,
typically fairly low dimensional.
You know, so maybe we're over
sampling observations from a given
state or from a given industry
in that case, like the state or
the industry would go into your X
and that's fairly low dimensional.
And so kind of that's fine.
And also it can be the case that X
is a low dimensional measure of U.
In fact, this is often the case
when you're choosing what data to
label, where you're using
some embedding distance.
You have a query, you know, this
article is about Polygon politics.
And then you have the embeddings
of your newspaper articles and
you over sample the ones near
the query to get more of them
that are positives.
And again, that that's fine because
that X is fairly low dimensional.
And so I wanted to make
a note here,
I mentioned this briefly earlier.
Typically the way that economists
deal with kind of the issue
of having severe class imbalance is
they say, okay, you know,
I'm only going to
label texts that have the keyword
pesticide in them and I'm going
to kind of ignore everything else.
And that's okay if
you're only interested in
texts that have the word pesticide.
But if you're interested in
alt text and you're going to run
your neural network over alt text,
then that is again going to be
problematic because you have no
idea how your neural network is
doing on texts that do not contain
that keyword.
And intuitively, like, we would
expect the measurement error of a
language model to be systematically
correlated with the terms that
appear in the text, right?
And so we talk a bit more in
the paper and point readers to
references on how to deal
with this sort of situation.
All right? And the final assumption
is mean squared error consistency
of the amputation function.
So intuitively, this condition just
says that we need the expected
square error of our estimator so of
our neural network to go to zero,
as the amount of data we train the
estimator with goes to infinity.
So in other words, the neural
network is well specified.
And this is very, very mild in the
context of deep neural networks.
So there's a recent theoretical
work that has shown that some.
Certain classes of deep neural
networks learned with gradient
descent, including transformers,
meet this condition.
And just intuitively,
if you trained your
neural network on infinite data,
it would give perfect predictions.
Okay, it's pretty,
pretty weak in this context.
All right, so as I mentioned, if
you as the researcher are the one
annotating your data, then your
annotation function is known.
But because you're the one who's
doing it right, and that's
the easiest scenario to be in.
Now maybe you're in
a scenario where somebody else
annotated the data and you don't
know kind of what that function is.
That assumption can be relaxed.
You can estimate it.
Then you're going to have to make
assumptions about the rate of
convergence of the neural network.
And I don't want to get into that.
But there's technical points about
this in the paper.
I mean, I think the bigger problem
is if you didn't label your data,
do you have any way to know that
that meets missing at random
is probably like the bigger problem
than knowing what that
annotation function is.
And so, you know, I can see that
all of this gets more complicated
if you're relying on somebody
else's labeled data and they do not
specify how they labeled it.
You can estimate that,
but, you know, did they use,
is it a representative sample?
Who knows?
All right, and so I wanted to speak
for a moment about
what I mean by efficient inference.
So a semi parametrically efficient
estimator achieves the lowest
possible asymptotic variance
of that estimator amongst all
regular asymptotically linear
estimators of that functional.
So this is, you know,
this is essentially a fancy way of
saying that that's going to attain
the semi parametric lower boundary.
Lower bounds are associated with
efficient influence functions.
You know, there's a lot more
technical discussions and
proofs in the paper.
I really don't want
to get into this.
I feel like if I talk too much
about econometrics after lunch,
I will lose everybody.
But I want you to just,
I want to just point out that,
you know, there's a lot of
technical econometrics in
the paper for anybody kind of
with that background that's,
that's interested.
It actually, I'm not
an econometrician, and so it took
me a lot of effort to understand
this literature, but I tried
really hard in writing the paper to
make it as intelligible to people
who know econometrics but are not
econometricians as possible.
All right, so that's efficiency
what do I mean by robustness?
Well, in the context of semi
parametric inference,
when we say that an estimator is
robust, that means that we have
constructed an estimator that
relaxes the rate requirements for
our first step estimates and
multi step procedures.
Right.
And so in the context of deep
neural networks,
we have a multi step
procedure because first of all,
you're using your neural network
to impute your structured data.
That's the first step.
And then you're using
that structured data to
estimate some quantity of interest.
And so the parameters from that
neural network and
kind of the language of
the econometrics literature,
those are nuisance parameters.
You don't actually care about the,
you know, 350 million parameters or
176 billion parameters in
the neural network that's been
estimated.
But you need those, they matter.
If those parameters are poorly
estimated, you're going to get bad
predictions.
And so we call those nuisance
parameters.
And in kind of this context,
in the first step you have the deep
neural network that you're
estimating and then you also have
your annotation function.
And we're going to assume in the
baseline framework that you don't
have to estimate that annotation
function because you annotated
the data so you know what it is.
And so robust estimators
are designed to tolerate trade offs
estimation error amongst
the first step components
while still maintaining asymptotic
normality and routine consistency.
And so
the basic idea is worse performance
in one component of your first step
estimation can be offset by better
performance in another component.
And you know, if we have two
estimators, this is called double
robustness, which is where the term
double bias machine learning in
the Chernozhukov sense comes from.
>> Speaker 2: And to the reversal
function, assuming there are also
inference questions as well.
So in some sense the machine
learning is a first stage estimator
and there's going to be some
standard error or something like
a standard error around
the parameters of that model.
And so just like in two stage least
squares or in the second stage,
we need to kind of adjust
the standard errors for
the variance of the first stage.
It seems like there's also
potentially kind of
a related influence point.
>> Speaker 1: Yes.
And so we wouldn't
know how to characterize that.
And so that's why we're treating
this as a black box.
And you know, so you could, yes, if
you knew how to characterize that,
you might be able to get more
efficient estimates out of there.
And there is some work, but you
know, by some researchers who have
Taken like a topic model, which is
a much kind of simpler model, and
they characterize that bias.
And then you can use that
to debias.
And so there's some work on that if
you're using something simple
kind of in the, in the first step.
But since we have no idea how to
characterize that for
a transformer, that's why we're
treating this as a black box.
And what you'll see is like,
the robustness is important here
because we can have arbitrarily
large bias in our estimation of
the neural network.
And that's okay
because we're trading off that bias
against the fact that we
know our annotation function.
We've annotated a representative
sample, and we're going to use that
to correct the bias.
Now, if we have infinitely large
bias and we try to correct it with
our ground truth, our standard
errors are going to be,
you know, are going to be large.
That big sample
is essentially telling us nothing.
And at the end of the day,
we only have our small annotated
sample to go off of.
Right.
>> Speaker 2: Seems like there's
a kind of a question there, right,
that there's an error in
the machine learning model.
And sometimes I'm not taking.
If I run my second stage regression
and I just compute
the usual standard errors, so
I do OLS on my structured data and
I just compute the standard errors
in the normal way, those
standard errors are not going to
sort of take into account that I've
actually generated their model.
>> Speaker 1: That has implicitly,
yes, but the biasing is taking
that into account.
So debiasing, like, one of the main
things we'll see is it can really
increase your standards errors.
But you're doing that, you're doing
that in essentially the way that
the measurement error literature
does that, and that you're not
trying to characterize what that
bias is because you can't,
because it's a transformer.
Instead, you're just trying
to empirically measure it and
to adjust for that.
And so kind of, that's exactly why
we need double robustness here.
If we didn't have double
robustness, then we would have to
worry about the convergence rate of
the neural network.
And we have no idea really like
what that is.
And it gets very
sort of very complicated.
But in this case, Mars is going to
be weakly doubly robust.
And kind of intuitively,
the reason for that is we're able
to have these very weak conditions.
Just what I showed you,
the universal consistency.
So we need the neural network to be
well defined.
If we train it on infinite data,
it would give perfect predictions.
But that's all we need is universal
consistency, because we have.
Access to the most accurate
possible first step estimator for
the annotation function, which is
the annotation function itself.
We're able to correct for that bias
by empirically observing it rather
than having to characterize it
in a kind of in a closed form way.
And by the way, we can get
rid of universal consistency.
So for instance, like
if you use ChatGPT, you, you could
put infinite data in there and the
error of it is not going to zero
because you're not training it,
you're just using it off the shelf.
And then you won't
have an efficient estimator.
But it can still be unbiased.
And in fact, most of the existing
statistical literature on black
box AI,
they just assume you're doing that.
You can just have arbitrary
bias in this.
It's not going away asymptotically,
but that's still okay
as long as you have this
representative ground truth sample.
>> Speaker 2: So in this context,
is there any advantage from
generating the annotated data on
the large sample multiple times,
for example,
with slightly different models or
with slightly different prompting?
That seems something that
in the past this literature has
not focused on because it was other
surveys of you humans and they're
not going to respond 50 times or
it was, this is one data set we
got and there is no ability
to regenerate it.
How would you
incorporate that here?
>> Speaker 1: Yeah, I think
that's a great question.
So you mean not for
your ground truth data,
like you still have a human label,
your ground truth data, but for
your imputed data you take like
an ensemble of models essentially.
Yeah, I mean I think like
we can definitely incorporate that,
right, because we know what
the ensemble of models predicts.
Again, it's a black box and in that
black box there can be an ensemble
like we know what the ensemble
predicts and we know the truth.
And so again, like all of this
framework, you could be using
a keyword classifier.
The big data sample could be your
RA who's doing maybe a poor job.
And the ground truth
is you doing it correctly.
And you could debias your
RA's predictions.
You could use like in that black
box can be kind of anything that's
an imperfect predictor.
And yeah, I mean whether ensembling
is going to improve the prediction,
I mean I think is that it's at
the end of the day it's
an empirical question, but
I guess you can measure that.
But yeah, certainly it's like
it's a possibility, but
it's going to depend on the air
structure of those Models and
probably exactly what you do
to ensemble them, like kind of how
much they're going to help.
But there is a machine learning,
a big machine learning literature
on ensembling.
Okay, so how do we implement this?
Well, first of all,
as I stated before,
we're going to need that your
kind of target parameter would be
identified if you didn't have this
problem of missing structured data.
So you know, if the person who
wrote the newspaper article
had started by saying this is or
this is not about economic policy
uncertainty, you just had that
your parameter would be identified,
then you need to derive
the efficient influence function.
And I mean in practice you don't
need to do this because we're going
to derive them for you.
Okay, but I'm just stating,
you know how you do this when you
do it from scratch.
We follow the method in Kennedy
2023.
There's essentially like three
different ways to compute efficient
influence functions and they kind
of have some different trade offs
in terms of how complicated
they are and finite sample bias.
And so we use kind of this,
this approach, which is kind of
used frequently in the literature.
Then we need to construct
the robust and efficient estimator.
And we're going to do that by
adding a one step correction to
a plugin estimator that's based off
the efficient influence function.
Again, there's
other ways to do this, but
that's what we're going to do.
These other ways would give you
the same result in the end, but
maybe they're
a little bit more complicated.
And we're trying to keep this
straightforward.
Okay.
And so we're going to do, you know,
we're going to do steps two and
three for you.
And so we know what the estimator
is and you're going to see
it's like super intuitive and
kind of obvious, I guess, ex post,
if you're familiar with some of
this literature.
But we do do all
the derivations and proofs.
And then so you have the estimator,
you're going to do sample splitting
for estimation.
Right. And this goes back to the
question that was already asked.
Your data that you're using for
debiasing, that data is only used
for debiasing.
You're not using
it to train your model.
Okay.
And you're not using it to kind of
estimate your, you know, it's,
you're not running, it's not part
of your big unlabeled data set.
You're just using that for
debiasing.
And it would be invalid if you use
that data to train your model,
because then obviously you'd be
overfit and we'd have no idea
what your bias was in the data that
you didn't use to train the model.
All right, so now I want to move on
to the different estimators.
And I think I'm going to go through
this kind of
quickly because, you know,
we could spend time deriving them,
but once you see the form that they
take, it's really intuitive.
And so again,
I'm going to illustrate this on
commonly used estimators.
I'm going to start with descriptive
means and
then go on to other estimators.
At the end of the day, all these
estimators are very similar
because these are essentially all
mean functionals, you know,
iv differences and differences.
At the end of the day,
these are all estimating means.
And so the estimators
are going to look pretty similar.
This framework only applies to
pathwise differentiable functions.
This is kind of true more generally
of these semi parametric inference
frameworks.
And so that's just a caveat.
And that's why we're doing
RDD under local randomization.
Okay.
And as I said,
all the estimators I'm going to
show you are essentially estimating
a mean of structured data.
And, and this is not horribly
important from a practical
standpoint, it's important from a
technical standpoint because we're
doing semi parametric inference.
We're not doing non parametric
inference because we're assuming
that your annotation function,
how you annotate the data is known.
If that was unknown,
this would be fully nonparametric.
And there's actually in semi
parametric inference,
there can be multiple
efficient influence functions.
And that can make deriving all of
this really complicated.
But we're able to prove that in the
case of these mean functionals, the
semiparametric efficient influence
function is the non parametric
efficient influence function.
And that non parametric efficient
influence function is unique.
And so that just simplifies
all the proofs significantly.
Intuitively, what is this saying?
Well, this holds because if
you label the data in a different
but valid way, you would still get
the same estimate.
So nothing is relying on
you labeling
that exact set of text or images.
As long as you have
this representative sample,
you could have labeled a different
set of text or images and
you'll still get, you know,
up to your confidence intervals,
the same, the same estimate.
And so that's why that holds.
Okay, so I'm going to start out
with the simplest possible example.
We have some
missing structured data.
We've imputed
that with a neural network.
We want to estimate the mean.
We can't do that on the truth M
star because we don't observe that.
Instead we have this
function mu that we're going to
estimate with a neural network.
And so we can derive the efficient
influence function and derive the
robust efficient one step estimate.
Estimator.
I want to kind of come to
the next slide and write this.
I'm going to write this in several
different ways
just to kind of make it more
intuitive what this is saying.
So the form that I wrote this
in first, for those of you kind of
more familiar with semi parametric
inference, you'll see that this is
the augmented inverse propensity
weighted estimator, which comes up
a lot in causal inference.
Let's kind of rearrange those terms
a little bit and
we get the second expression.
And you see there, there's a term
that is essentially that u hat term
that's taking the mean of your data
from your big sample, your
predictions from your big sample.
So that term A would be your
estimate if you ignored the fact
that you had imputed this data.
So it's just the mean of,
you know, is this article about
economic policy uncertainty?
Yes or no?
Okay.
And then the second term there is
your correction term.
And so you're taking the difference
between your ground truth and what
you predict and averaging that.
And it's
inverse propensity weighted, right?
Because you're weighting by
the propensity, the data with those
observables are in your sample.
So but essentially you're just,
you're averaging that difference.
And so basically,
if there's a big difference between
your ground truth and your
prediction, the variance of this
term is going to be really large.
If you have a really small sample,
the variance of this term is also
going to be larger.
And so
what you're doing is essentially,
maybe it's even easier to see this.
I'm going to rewrite this again.
And this comes from a paper by List
et al, which he calls flexible
regression adjustment.
And here what you do is you take
just the estimate in your ground
truth, so what you labeled, and
then you're going to adjust that
with this adjustment term that
leverages your full sample of data
you imputed, but accounts for
the differences between that and
your ground truth.
And so this is essentially
has the same intuition as
a linear regression adjustment.
We adjust for those systematic
differences between our large
unlabeled sample and
our small annotated ground truth
sample, and use that approach.
And so essentially,
at the end of the day, it's saying
we have this ground truth estimate,
we know that's identified, but
we want to leverage our big sample.
How do we combine these two things?
You can think of that as just like,
here's the estimate in our ground
truth sample, or sorry, here's the
estimate in our full big sample.
And then we're just going to adjust
that by the difference
between our ground truth and
our predictions weighted by,
you know, the propensity of that
being in the sample.
And our standard errors are going
to account for the fact that that
is measured with uncertainty.
So that term, even if there's our
n of our full sample, is huge.
And so let me go back.
So the variance on this term,
the first term, is tiny.
The variance on term B
is going to be really big.
If you have a terrible model,
that term will be big
because that difference is big.
On the other hand,
if you have a perfect model,
this term goes to zero.
Right? And it's just like using
the predictions from your huge
sample, which is going to have.
And maybe this kind of like
goes back to your question about
why not just use the small sample.
Well, if the big sample is way,
way bigger,
you're going to get like,
essentially, you know,
super tiny confidence intervals.
If your model is super,
super accurate, you
can really leverage that full data.
All right.
Yes.
>> Speaker 2: So in the last slide
for the annotation, the function is
taking in the argument X,
which is the covariates.
But I would have thought that
the annotation would want to take
in the unstructured data and
then annotate that.
So I guess I'm having some
difficulty understanding
what exactly as simple as like,
this is a.
>> Speaker 1: Okay, sorry,
it's my fault for kind of maybe for
going through this too quickly.
And so X is essentially kind of
the covariates that you observe.
But then what's in parentheses here
is X tilde, which is
the combination of X and U.
So that is your unstructured data
going into that.
>> Speaker 2: So couldn't that be
insanely high dimensional for
each data, for example?
>> Speaker 1: It's insanely high
dimensional.
But what we need is that the neural
network is universally consistent.
So I think if we thought that
neural networks couldn't handle
the insanely high dimensional data,
then they would be useless in
some sense.
And so we're assuming here that
it's okay to feed high dimensional
data into the neural so
mu hat is your neural network.
Right? And so kind of the basis for
all of this is like that you can
feed high dimensional unstructured
data into a neural network and
get something reasonable out of it.
And that's
a legitimate thing to do.
>> Speaker 2: When you're doing
the inverse propensity,
your probabilities could be very,
very high.
>> Speaker 1: But we're not
choosing what to annotate
based on mu, we're only choosing
what to annotate based on X.
And so this goes back.
Where did I talk about this?
To this idea of strong overlap.
And so this annotation function,
when we decide what to annotate,
this is based on X and not on U.
And X we're assuming is low
dimensional.
And you're absolutely right that
if X was high dimensional,
then strong overlap is implausible.
>> Speaker 2: I see. So
strong overlap allows us to be.
>> Speaker 1: Exactly.
So we're assuming X.
So what makes your labels
representative?
What gives you unconfoundedness
is not too high dimensional.
I know there's a question
about what that means in practice,
like an empirical question, but.
Yeah, that's very important.
Sorry. As I
get back to where we were.
All right, I'll skip over.
This is closely connected to Debias
machine learning.
But since that's a little bit
tangential, I'll just kind
of acknowledge that and you know,
and move on linear regression.
So, and I should say kind of in
these examples, X is going to be.
Or, you know, and the data that
we're imputing is going to be.
It could be an outcome, you know,
or a treatment.
I'm going to, you know,
I'm going to show one example.
So in linear regression,
your missing data is your outcome,
but that could just as easily be
something on the right hand side.
And it would.
Everything would be
fully analogous,
which I think you'll see kind of
intuitively as we go through this.
So we have some.
We're imputing our outcome with
a neural network and then we have a
series of regressors, C. All right.
And we want to do valid linear
regression.
You know, I'm going to apply
Frischois again.
I don't want to focus too much
on the derivations, but we can form
the efficient influence function.
And we see here that
this is kind of.
This is the estimator that we get.
And you know, so if you remember
standard linear regression, you
know, X prime X inverse, X prime Y.
That's essentially what
this looks like.
But remember.
Y, the outcome is you're missing
structured data.
So when you have X prime X inverse,
X prime Y, the Y is that term in
the square brackets
which is exactly the same term for
mean estimation.
Like, why is that?
Well, at the end of the day,
linear regression is also a form of
mean estimation.
Yeah. In these regressions, are you
putting the ML, the output of the
algorithm on the right hand side?
The left hand side,
it doesn't matter.
This is on the left hand side here.
And so that's why
it's like in the Y place.
But if it was on the right hand
side, that's absolutely fine.
And it would just be
that you're doing that adjustment.
Like C is just fresh wad,
like the, you know, the covariates.
The adjustment would just be on
whatever C, or it could be multiple
Cs, and that's fine too.
It would just be on whatever C and
you'd just be doing the exact same
adjustment.
Right. The same as you do for mean.
That's it. It's just like
your outcome.
You just adjust it in the same way
you adjust the mean.
And I kind of
tried to show this here.
You can think about this as just
a residualized regression that you
run on like this pseudo outcome,
which is just your kind of debiased
Y, your debiased outcome.
And everything is going to
take this exact same form.
Before I get to that,
I will say that one interesting
thing that comes out of this is
that the imputation function,
your neural network,
if you want efficient estimates,
it's a function not just of
your unstructured data, but also of
your C, other control variables,
relevant things in your regression,
as long as they're not orthogonal
to your outcome, which I
think is kind of interesting.
But in any case,
I want to move on to linear iv.
And so now here we have
an instrumental variable Z, and
we have our outcome Y.
And in this case we're going to
assume that our missing data that
we're imputing is the treatment.
Okay. Again, it could be any of
the variables in the regression,
but for the sake of illustration,
we'll say that it's the treatment.
If we kind of skip forward to
the expression that we derive,
again, you know,
it's your standard IV coefficient.
But now like where the treatment
would appear, you're adjusting it.
So once again it's like
as if you're running this
pseudo TSLS regression on your
pseudo treatment, which is just the
debiased, you know, the debiased
data that you've imputed.
Right. And so Again, it looks like,
you know, it looks like the exact
same as the mean expression and
the term where you're kind of your
treatment enters.
But you're just doing that same
debiasing that we talked about,
a mean estimation,
differences in differences.
I know there's a lot
of notation here that I'm going
through quickly, but we essentially
think of differences and
differences as just.
It's a difference in two
means right at the end of the day.
And so
you can see it's the exact same,
you know, the exact same thing with
some additional notation that I
know I've gone through too quickly.
But. But essentially you're taking
the differences in these means and
you're adjusting them for
the fact that they are imputed with
your neural network in exactly
the same way where you have
the raw predictions from your
neural network and then you have
this debiasing term that measures
the difference between
your neural network predictions and
your ground truth weighted by the
propensity of that ground truth, K
of being a near full sample in rdd.
Again, now we're going to assume
the missing data is the outcome.
RDD is also a difference in means
right at your threshold.
And so again, the estimator looks
essentially similar.
You're debiasing your outcomes for
the amputation error.
All right, I want to talk
briefly about extensions, and
then I do want to leave time to
give some empirical examples.
And so the first thing I want to
talk about is a world where you
want to aggregate your predictions
from the neural network.
Right. And so it's almost,
you know, in my experience,
looking at a lot of papers,
typically not the case that your
regression is at the level of your
text or images, typically you're
aggregating them often you're
transforming them nonlinearly.
And so how do we deal with that if
you're transforming them linearly?
It's pretty straightforward.
The way that we deal with this in
a much broader setting where you
can have nonlinear transformations
interactions is
essentially very intuitive.
So let's say you have some
regressor in your model X1.
It could be multiple X's, but
let's say it's X1 for simplicity.
And you're imputing that with
a neural network.
And then you're aggregating up and
potentially transforming X,
which is your sort of your
treatment of interest.
And what you can do is to just
estimate the mean of X at whatever
level you're aggregating with,
with the Mars mean estimator that I
showed you guys a few slides ago.
And now that is that is unbiased.
So that we know from what I showed
you earlier that now you have
an unbiased measure.
Let's say you have an unbiased
measure of economic policy
uncertainty in the United States in
1997 and now you want to run
regressions with the log of that or
with that interactive with
something else.
Well, now you have the unbiased
estimator and
there's just one catch.
It might be unbiased, but it still
has classical measurement error.
Right. And so, you know,
if we go through, let me see if I
can just pull this up again for
the sake of.
That's not going to work.
You know, if we go through and
we have here this, you know, this
unbiased estimator, it's unbiased,
your mean is unbiased, but there's
still classical measurement error.
Right.
And so you can just plug in that
unbiased measure of the mean.
But you do need to adjust for
the fact that there's classical
measurement error in it.
Right.
And doing that is very
straightforward.
So that goes back to the question
from a while ago,
you know, kind of,
what about this survey literature,
work by Deaton, et cetera.
That literature was
primarily assuming classical
measurement error.
And it's well known how you adjust
with, for classical measurement
error with gmm.
I won't go into that now, but
you can do this in Stata, and
it's very simple and
it's been around since the 80s.
And so the basic idea,
again, I know I'm, you know,
going quickly through this,
but let's, I'm going to get to this
real example in a minute.
So let's say you want to measure
economic policy uncertainty at
different time periods in
the United States by aggregating up
millions of predictions from
a neural network where you say,
does this newspaper article talk
about economic policy uncertainty?
Well, you know, the problem is we
don't know the ground truth.
Economic policy uncertainty in 1997
in the United States,
that's a population level quantity.
So we can't apply kind of standard
debiasing which assumes, you know,
the ground truth.
But instead what we're going to do
is economic policy uncertainty in
the US in 1997, which is kind of
one of the variables you
want to enter your regression.
That's a mean and we estimate that
using the mars mean expression.
And now we have an estimate,
an unbiased estimate of economic
policy in the US in 1997, but
it still has classical
measurement errors.
So we can run our regression, but
we just adjust for
the classical measurement error.
And why don't I.
I'm going to skip over.
Maybe we can come back to this if
we have time, but
I'm going to skip over
how to decide how to annotate data.
I know that.
That's important.
But that also
opens a lot of questions because I
want to get to the example.
So I keep on talking about economic
policy uncertainty,
because this is kind of an actual
example that we use.
So this is a 2016 paper.
I'm sure everybody knows it.
It has like 16,000 citations.
And so the goal of this paper is
they want to measure economic
policy uncertainty.
They do that by taking newspaper
articles and predicting
the share of articles each month
that talk about policy uncertainty.
And so this is a 2016 paper.
So they're not using
a large language model.
Right. They're using
a keyword search.
And so what we're going to.
And they also have a really large
ground truth sample,
which is super helpful.
So we're going to do
several things.
We're going to take their keyword
search measure, and
we're going to debias that.
And this is what I said earlier,
that debiasing.
It doesn't have to be
a neural network.
It can be any technology
in that black box.
So we're going to
debias their keyword estimate, and
then we're also going to take their
validation sample and
do sample splitting and use part of
it to train a neural network and
then use part of it for debiasing.
Right. And so we'll get
a comparison between
different estimates,
which is what I have here.
And so the pink is there, you know,
what appears in their paper,
Economic policy uncertainty
measured with keywords.
Ignoring the fact that this was
imputed.
Right. Just treating
it as the truth.
The blue line is what happens if
you use longformer,
which is a large language model.
We use it because
some of the texts are larger.
If you use longformer and
treat that as the truth.
And then the yellow line is you
take their keyword measures and
you debias them.
This is again, just using
that expression that we looked at
to debias, a mean, because that's
all economic policy uncertainty.
And each year is just a mean
over all the newspaper articles
in that year.
And then finally, the green
line is debiasing the long former.
I think there's a few things here
to note, you know, so first of all,
the confidence intervals
are much tighter.
If you ignore the fact that.
That these data were generated.
Obviously, we could
make the Debias estimates tighter
by estimating better models or
by having a larger annotation set.
We're not doing that because we're
using their annotated data.
Okay.
I don't want to be the one labeling
economic policy uncertainty.
I'm using their Truth,
but you do see it reflected in
the standard errors.
Of course, the long former,
the neural network is more accurate
than a keyword search.
And so you see those standard
errors are a bit tighter.
And you know, the bias is not huge,
but you see a little
bit of systematic downward bias
relative to the Debias estimates.
Okay, so now the primary reason for
this exercise is that they want to
run regressions with it.
So this is one example regression.
They're going to take the change in
employment and regress it on
the change in log economic policy
uncertainty interacted with
this intensity measure.
And they have some
other things in the regression.
So this is a case where they've
aggregated up the predictions and
then they're transforming them
nonlinearly and
they're interacting them.
Fortunately, if we just estimate in
each year exactly,
we just take the estimates from
this figure and we account for
the fact that this still has
classical measurement error.
It's, you know, the debiased ones,
the yellow and
green, they're unbiased now, but
they still have the classical
measurement error left.
We account for that.
This is what we get for
that regression.
And so the ones on the left hand
side, these are accounting for the
fact that when we use these mean
estimates in this regression that
they're still estimated with error.
And so we're just using
standard techniques to correct for
classical measurement error.
And you see the keyword measure and
the neural network, the long former
measure, those are giving us kind
of very similar point estimates.
The long former measure has
a tighter confidence interval
because it's a more accurate model.
On the right hand side, we're just
taking these and plugging them in,
kind of ignoring the fact
that the blue and pink ones
are biased and that the orange and
green ones, while unbiased, still
have classical measurement errors.
We just plug these estimates right
here, like into this regression.
And you can see here kind of
very clearly in the gray and
the pink, those are plugging
in the D bias estimates.
You see the classical
measurement error, right?
It's attenuated like,
no shock there.
We know what classical measurement
error in our right hand side
variables does it attenuates.
In this case, you happen to look at
the, the blue and the green,
which is just taking this, ignoring
the fact that it's been, you know,
estimated with a neural networker
with a keyword classifier and
plugging it in,
it actually looks really similar
to the unbiased estimates
that account for everything.
Why is that?
Well, that just happens to be
a coincidence of this particular
situation because
there's a classical component.
Right.
There's a classical component and
a non classical component
to those blue and pink estimates.
And in this case, you know,
the classical component,
it's attenuating it.
But the non classical component,
this index is a bit biased down, so
that's pulling it away from zero.
Those two things happen to exactly
cancel out, you know,
which is good.
And I wouldn't, to be honest,
want to show an example in this
paper where I overturn somebody's
results, because that's not like
a fight I want to get into.
So their results are great.
You can believe their results.
Of course, the confidence intervals
are larger when you account for
everything, but
obviously not in every situation
will the different components of
your measurement error cancel out.
I want to look in the last few
minutes at kind of one other paper.
This is a similar paper in that it
was inspired by the EPU index,
but they're looking at geopolitical
risk instead.
They're doing the same thing,
measuring geopolitical risk in each
year based on newspaper articles.
They also use a keyword search, but
we will take their audit data and
train a classifier.
So here you can see some really
substantial sort of downward bias.
The pink is their keywords.
The blue is with distil.
Roberta.
A neural network classifier.
It's still downward bias, but
not as much because the neural
network is a bit better.
And the green and
the yellow are the bias corrected.
And basically in their ground truth
audit sample, a very high share of
articles during the world wars and
to a lesser extent September 11th
are talking about
geopolitical risk.
And their keyword classifier
misses a lot of those.
Right? So it has good precision but
not very good recall.
So that's going to lead to this
substantial downward bias.
And by the way,
this is very common, especially
with keyword classifiers.
Language is complex.
There's a lot of way to see things.
So it's easy, easier to get good
precision than good recall.
Now we're going to look at
a regression, this regression,
the regressing disaster
aid on geopolitical risk.
Okay? And geopolitical risk,
this is just an annual time series.
Okay. It's literally like the pink
dots in this regression, right?
That's what they're plugging in.
So they're plugging in the pink
ones, but I'm going to plug
in these different ones.
The same thing as for
the EPU exercise.
And you see here again, you know,
kind of something fairly similar.
It doesn't make
a huge amount of difference.
To adjust for the classical
measurement error, you see?
See some bias in their blue and
green estimates.
You know, in this case, they really
have very few observations because
this is just an annual regression.
So there's like,
sampling variance issues.
Again, there's differences in
the point estimates.
They're not huge.
Why is that?
Well, you know, clearly, you know,
the world wars were a very
economically destructive period.
And even with the biased indices,
geopolitical risk goes up during
the world wars.
And that's what's
driving these coefficients.
But I think we can think of many
examples where the effect might be
more subtle than the impact of
world wars and the probability that
there's an economic disaster,
which is essentially what this is
picking up.
So this is again, just to say,
I've given you another example
where it doesn't radically change
our coefficients, but you
could imagine other scenarios where
the change might be bigger.
It's still the case that the world
wars are the main driver of
economic disaster in this figure.
And they have a lot of other
regressions in their paper.
I'm not saying this is
the main one, but
this is just what we chose to do.
A quick note on design choices.
This is varying the size of
the annotated data.
Obviously, you know,
this was your question.
You get more precise as you
annotate more data.
Part of that's just you're
getting a better model because
you're split, splitting your
annotated data between training and
debiasing.
But it also kind of helps with
standard errors from
the debiasing side.
And so this is
just the share of our sample.
You know, I think this is in
the range of a couple of thousand
articles labeled.
So it's not huge sample.
This is varying
the accuracy by using different
neural network models that have
varying degrees of accuracy.
And the blue line is just using
the truth.
And again, you can see that as the
model gets better, your standard
errors get tighter, although,
you know, kind of after a while.
This is 85%, 90% accuracy.
With Modern Bert,
it's getting, like,
pretty close to the ground truth.
But if you're down at, like,
it can make a big.
There's a big difference between
like 75% accuracy and
like 90% accuracy, which is.
I think we could sit here and
argue what's good enough, but
here in this figure, you see it.
And like, 90% will give you tighter
standard errors for sure than 75%.
All right, so
I think I am out of time.
So just to kind of sum up,
deep learning provides powerful
tools for processing data.
Hopefully you guys saw that in
the first lecture on this morning.
But we do want to take into account
that these models are not perfect,
that neural networks measure things
with AIR and incorporate that in
a principled way.
And we do that by essentially
combining this new literature on
black box AI and a much older
literature on semi parametric
inference for missing data.
And we apply this framework
to a variety of common
empirical scenarios and
show that accounting for imputation
bias is important and can influence
both your point estimates and
uncertainty quantification.
All right, thank you.
