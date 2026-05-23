---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: de74ac8d-b7fa-4b3c-916b-e9caec95a01b
source_title: "Deep Learning in Economics I"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:35:24 UTC
extractor: nlm_bulk_extract.py
---

# Deep Learning in Economics I

## NotebookLM-extracted transcript (Google's ASR + indexing)

Thanks so much for the invitation.
And so today I want to talk about
deep learning in two parts.
And so the first part, which will
be at least mostly before lunch,
I want to talk about the machine
learning side of things, about how
we use these tools essentially to
process unstructured data,
by which I mean things like text,
images, audio.
And then after lunch,
I want to talk about
the econometric side of things.
Right. So now you've used some of
these tools to take unstructured
data, to take text images, to
incorporate it into your research.
But you want to get
the econometrics right.
You want to account for
the fact that you've done this,
that this data, that these
predictions that you've used deep
learning to predict, they're not
the truth in some deep sense.
They're probably measured with air.
How do you account for that?
How do you get the
econometrics right?
And so we're going to have
kind of these two separate parts.
And, you know,
if this goes over a bit,
that's fine.
We don't have to spend the entire
hour and a half on econometrics.
And I'm going to have a really
heavy emphasis on examples.
And so these might not be examples
that everybody is kind of
personally interested in, but
hopefully they give you a flavor
for how these tools are used.
I'm not going to go into
technical details, you know,
that could take an entire course,
but I have a website and you'll see
the link in these slides that point
to lots and lots of technical
resources that have lectures.
And so for people who
are interested but
kind of want more information on
the technical side of things, I'll
point you in the right direction.
All right, so with that said,
we'll go ahead and get started.
I don't know if you have like
a procedure on questions.
Do people want to jump in if.
>> Speaker 2: Anything, or
whatever you prefer.
>> Speaker 1: Okay, yep.
If anything is unclear, jump in.
We'll also try to leave some time
at the end just to have like
a broader discussion.
But if I've lost people, please do,
please do let me know.
All right, so deep learning has
revolutionized the processing of
unstructured data.
And I said unstructured data
are data that
you know are too high dimensional,
too complex, too uninterpretable to
plug directly into your analysis.
And so what you want to do is to
use deep learning to extract
information that you can then
understand and analyze directly.
You know, in economics,
we might think about extracting
sentiment or topics from text.
You know, in other fields they
might be Extracting information
that they can use for a self
driving car or to diagnose disease.
And so deep learning
has transformed kind of all
these disciplines by making it much
more feasible to accurately and
on a large scale extract
information from unstructured data
that can then be used to perform
whatever analysis that you happen
to be interested in.
And so
within economics specifically,
we have massive quantities of data
in their raw form that you can't
really compute with that could
transform our analyses if they're
processed into a format that can
then be used for computations.
So text is probably the prime
example.
Huge amounts of information there.
Data can also be tracked in images,
you know, whether that be images of
documents from archives,
satellite imagery, aerial
photographs, social media images.
There's also audio and video,
which is essentially a bunch of
images in rapid succession that's
combined with audio.
And so while this raw information
is very different, the methods that
we use to convert images or text or
audio into computable information
are quite similar.
And they typically will draw on the
same neural network architecture,
which is called the transformer.
So you can use a text transformer
for text and kind of all the large
language models that you've
probably heard of are transformers.
You can use an image transformer
for images.
Actually, interestingly enough,
the state of the art model for
audio was pre trained first on
a large number of images.
And so the architecture is just
kind of very similar.
Then they use
the image of the audio spectrogram
of the waveform created by sound
to analyze the data.
And so you can have very different
types of data, but the toolkit is
essentially very similar.
And so our goal in processing
unstructured data is to take this
complex, diverse information and
learn a mapping into a format
that is easier for
us to process and to understand.
And so if you want to say that kind
of in a technical way, we're going
to take our high dimensional text.
You know, think of raw text
as a bunch of sparse vectors.
The dimensionality of the vector
is the size of the vocabulary.
So if it's English text,
it might be the size of
the English language.
That's all zeros except
a single one,
which is the word that is used.
That is a very difficult object to
compute with.
Think of an image as RBC
pixel data.
Again, very
complicated object to compute.
We're going to take those
complicated objects and map them
into a continuous vector space.
And what I mean by that is
you're going to say,
take a patch from your image or
a word out of your text and you're
going to Map that into a vector
that's much lower dimensional.
Like 512
would be a typical dimensionality.
And it's going to have numbers in
every position of the vector.
And we know how
to work with those low dimensional
vectors really well.
So at its core, deep learning is
an approach for learning these
representations, these continuous
vector representations of data
from empirical examples.
And so in deep learning you don't
tell the computer the rules that
you're going to use to map that
high dimensional data into
something more low dimensional.
It learns how to do that
from empirical examples
that are fed to the model.
And so you might be
wondering at this point, why are we
going down this route at all?
Why use a neural network to
transform the raw data versus just
trying to work with them directly.
Or you could have using existing
methods like say
a keyword search in the text.
There's essentially three reasons
why neural networks are so powerful
and so transformative when it comes
to working with unstructured data.
The first reason
is transfer learning.
Deep neural networks incorporate
relevant information
in their parameters from exposure
to massive scale data.
And so, you know, state of
the art language models nowadays
they've seen trillions of tokens of
text in their pre training.
I think it's hard for
us to comprehend just how much text
that they have seen.
Okay. Whereas if you devise your
kind of omad that it's just
relying on whatever information
you bring to the problem.
With deep neural networks you can
leverage a model that took millions
of dollars to train on trillions
of tokens of text and it basically
already understands language and
now it just needs to understand
your problem like as
a subset of that.
>> Speaker 2: That in a sense one
can sort of think about
information loss.
So we kind of reducing dimension
and in a way we may just be kind of
getting rid of a lot of relevant
detail and encoding the information
we want to work with.
But in some sense there's also
potentially information loss.
Right. Or there's a motion.
Is there a sense in which one can
sort of think about
that dimension reduction and
whether we're extracting
something informative or whether
we're losing something relevant?
>> Speaker 1: Yeah. So
I think that like if you want to
think about neural networks in
a broad sense and what they do,
I think kind of one powerful way
to think about them is there just
a technology for compression.
And so let's say you can take the
entire Internet, which is just an
unfathomable amount of information,
it's trillions of tokens.
You train this model and
essentially what you've done is.
Is to compress it.
Like let's say in the case of GPT4,
it's like 176 billion parameters.
And so you've taken trillions of
things and you've compressed it
down to billions, which is a huge,
huge reduction
in the size of the information.
And yeah, I think that
that's one way to think about it.
And of course there is loss.
These models cannot perfectly
reproduce every text that
they've ever seen.
And I think the question becomes,
is that loss
kind of relevant for your.
And it may be that you need to tune
the model on your own data rather
than using it off the shelf and so
that its parameters learn to attend
to the most relevant information
for your problem.
All right, so the second reason, I
know this is basic for some people,
but I do want to kind of go over
this because I don't want to assume
everybody has a lot of background.
And so the second reason why deep
neural networks are so powerful is
is they take into account context.
And so if you were just to take raw
pixels from an image or words from
a text and map them to vectors
without thinking about the context
they are in, that's going to,
you know, that's not going to be
a very effective way to do things.
Because the meaning of a word,
the meaning of a pixel depends on
the context.
Words can change
meaning drastically if you put
them into different contexts.
And the transformer architecture
really excels at being
map the context in which a word or
in which a pixel appears into
the representation,
the vector representation of that
word or pixel.
And then finally, deep learning
makes problems incredibly scalable.
And so it's really
unwieldy to work with raw text or
image data, whereas there's
extremely optimized tools for
continuous vector computations.
You know, so for example,
in some work that I did,
we were able to make 10 to the 14th
exact vector similarity
calculations on a single mid range.
By now quite old GPU card.
In a few hours
there's a library called
Facebook AI similarity search.
It was made by what at the time was
fair, what's now meta AI.
And they just made it public.
And it makes vector similarity
computations at incredible speed.
When you can get your data
into this continuous vector format,
it's incredibly quick with
modern GPUs to make a very,
very large number of calculations
in a very small amount of time.
And so you can do problems
at an unprecedented scale.
All right, so
this is just an illustration of
what I mean by context.
And at the top of the image you see
kind of figure representation of
how bag of words works.
And so bag of words, which was used
traditionally in nlp, you know,
essentially for
each word you separately map that
to a vector and then you have some
feed forward neural network layer
that maps that into probability.
Say like is the sentiment of this
text, positive, negative or
neutral, kind of.
And each representation for each
word depends on just that word.
Whereas with a neural network,
what we're going to do is take
these broad texts and feed them
into some complicated function that
then takes into account the context
in which each term appears.
I think if you learn one thing
about neural networks, it's that
deep neural networks are the state
of the art tool for estimating
really complicated functions.
And that's essentially
kind of all a neural network is,
is a really complicated function
that you're going to estimate by
learning from empirical examples.
So computation has a long history
in economics, but I think it's fair
to say that in the 1990s, the
advent of personal computing really
revolutionized the discipline.
Economics used to be
primarily theoretical,
it became much more empirical.
It's hard to imagine development
economics existing without personal
computing, which makes it possible
to easily collect your own data.
And I think today, kind of,
we're in the midst of a similarly
transformative time where advances
in GPU compute and the availability
of very cheap cloud compute
again have the potential to
transform the types of data and
questions that we can study.
For a relatively small amount of
money, I can spin up 1000
cheap CPUs on Azure,
run them all day long, and
it's going to cost me maybe $100,
maybe even less,
depending on the type of CPU.
I obviously could have never had
1000 CPUs use in my office.
And so once I have a neural network
trained, I can just process data
again at an incredible scale that
would have been unimaginable,
say 15 years ago.
>> Speaker 2: Melissa, do you think
there can be any trade off there?
Because you could argue that
in some sense we could
also lose something, right,
in terms of the ability of theory
to impose structure as to what
are the relevant dimensions of
the data and test mechanisms.
Do you think there's any kind of
potential trade off?
>> Speaker 1: I'm definitely
not saying that we should abandon
theory.
I don't know,
maybe people think we're going to
go crazy over neural networks and
that's what's going to happen.
Like, yeah, so
I'm not making a statement that
we should abandon theory.
And clearly every paper that you
write will have an opportunity cost
that you're not doing some other
type of research.
And so I'm certainly not advocating
that everybody should be using
the deep neural network and
doing exclusively big data work.
I mean, I do think that there's,
you know, there's sort of this
tension, I guess, between
the way that we traditionally
do things as economists and
the way that these tools work.
And, you know, maybe we'll get into
this a little bit more after lunch
on the econometric side of things.
You know, you're not going to
characterize the convergence rate
of, you know, 176 billion parameter
deep neural network.
But, you know, I'll talk then
about, you know, ways we can think
about deep neural networks from
an econometric standpoint, and
that treated us a black box, but
still fit within our traditional
models that we've had for
decades to think about things.
You might say that there's
a similar tension with theory that
you might get this neural network
that's incredibly predictive, but
we have no idea
why that is the case.
I think that that, again, is
a tension that has to be navigated.
I'm not a theorist and so
I'm not the best person to
speak about, about that.
But I do think that there is this
tension between, like, okay, we
fully understand what this thing is
doing, but it's really inaccurate
because the real world is super
complex versus, okay, we have
a very predictive model, but we
have no idea why it's predictive.
And I think, you know,
there is people,
people are thinking, thinking about
how, how to navigate this tension.
And I think there's going to be
a piece coming out in the JL about
neural networks and theory and kind
of trying to navigate that tension.
And so people are thinking, but
it's definitely a huge
open question.
All right, these are awesome
questions.
All right, so
what I'm going to focus on today
is using neural networks to make
predictions from unstructured data.
And so the kind of basic framework
that I want you to have in mind,
and I'll kind of develop this more
formally when we talk about
the metrics later, but essentially,
let's say you have like 50 million.
Newspaper articles.
You can't plug those newspaper
articles directly
into your regression.
You just want to know how many of
those newspaper articles talk about
economic policy uncertainty.
And so essentially
what you want is a 0:1 value for
each newspaper article.
Does this discuss economic
policy uncertainty?
But you don't have that.
You know, the newspaper didn't
publish that information when they
published the article.
And so your
goal is to impute that information
with a deep neural network.
And so that's the type of problems
I want to talk about today.
There's also lots of other
really fascinating uses.
Like people are using
deep neural networks to approximate
solutions to NP hard problems.
And I think that's super
interesting because while they're
not necessarily
better on a given problem than
traditional techniques,
they scale like way better.
And so you could
solve a really complicated
routing problem or something.
As I said,
there's applications in theory,
there's tons of applications.
I could
possibly talk about all of them and
I'm not qualified to talk about all
of them like in a short lecture.
And so what I'm going to be
focusing on is you
have a piece of unstructured data,
so like typically a text or
an image, and you want to
measure something in that.
Like how do we do that?
And conceptually
I'm going to divide these problems
into three different groups.
And if this doesn't make a lot of
sense now, I'm going to
give you lots of examples.
And so the first type of problem is
you want to impute
some continuous number.
So let's say you
have some satellite images and
you want to locate in those images
where street vendors are located
because you're trying to measure
economic activity.
So essentially you want to impute
the coordinates of the street
vendor and the image
that's a continuous number.
So in machine learning we call this
a regression problem,
not to be confused with regression
in the way that we
typically use it in economics.
So when we're in machine learning,
regression means we want to predict
a continuous number.
On the other hand,
we might want to impute
a pre specified discrete class.
And so in the newspaper article
I gave, we want to know, is this
about economic policy uncertainty?
Yes or no?
You know, that could be
multi class, you know, it could be
multi label, which is the, what we
call a classification problem.
When you know, a given text or
image can fall into
multiple groups.
You know, so this is about,
you know, both, you know, the labor
force and domestic issues.
And that's in the same
newspaper article.
What's important here is these
classes are pre specified and
Then the third type of problem
which we'll see actually comes up
a lot is that we want to impute
relationships in data where the
classes are not specified ex ante.
Or so you're in a world now
where you have this big data set,
you want to go explore it, but
you don't know, you know, you don't
know what the classes are ex ante,
you don't know what the topics are,
you know, et cetera.
And so we'll see lots of examples
of this type of problem.
Okay? So those are kind of three
different and distinct, and the
methods where you're going to use
for them are going to be distinct.
And these are kind of the main
three types of problems that
we have when we're trying to impute
something from unstructured data.
And so the basic idea is we have
this neural network and it's going
to encode this unstructured data
into these low dimensional
vector representations, right?
They're low dimensional,
they're dense, they
have a number in every position,
they take into account the context.
That's what the neural
network does.
Okay? And so the researcher can
either use these representations to
predict whether the raw data belong
to a pre specified class, and
there you just add a classification
layer which is going to map these
vectors into class probabilities or
regression works analogously,
if you add a layer to the neural
network that combines those vectors
that you've predicted to represent
your text or image, it takes those
and maps it to a continuous number.
Broadly speaking, generative AI
performs classification.
And so what say GPT is doing
is you feed in your prompt at each
kind of time, step in the text,
it's predicting a vector, a dense
vector, and then it's mapping that
vector to the most likely word in
the English vocabulary.
And there's some
stochasticity in there.
You can change that
with the parameters as those of
you who played around with it know.
But like the basic idea is it's
creating kind of vectors
at each time step in your text
to predict the next word, and
then it takes those vectors and
it maps it into what's the most
likely word in the vocabulary.
And so we can think of generative
AI as also a type of classifier.
But the alternative
is that you don't have to add that
classification layer to map those
vector representations of your text
or image to class probabilities or
to a continuous number.
You can work that directly
with those vector representations.
And these are referred to as
embeddings.
And we're going to see lots
of examples
where it's advantageous and makes
the problem kind of much easier to
work directly with those vectors.
All right, so
this is like a classification
flowchart.
So suppose you have, you know,
like, let's just say that you have
some text, maybe it's posts from
social media, maybe it's news
articles, et cetera, and you want
to group those into classes.
What tool might you want to use?
And I'm going to go into this in
a little bit more detail, but
this is just an overview.
So there's a series of questions to
ask yourself.
Are the classes no?
And ex ante?
If the answer is no,
you cannot add a classifier later
to your neural network
to do predictions because you
don't know what the classes are.
A classifier layer maps
directly to pre specified classes.
So if you don't know what
the classes are,
say you don't know what the topics
in this data are, you cannot use
kind of a traditional classifier.
Instead you have to
work directly with the embeddings.
On the other hand, if the classes
are pre specified, ask yourself how
many classes there are.
You know, if there is a lot,
like say, you know, 100,000,
you're not going to be able to
compute the classifier layer and
forget doing a classifier.
But even if there's less than
100,000 to train a classifier,
the model needs to see
all those classes in training.
And you might not have labels for,
you know, 10,000 classes, right?
And so if you don't have labels for
everything you know, again,
you might want to use embeddings.
On the other hand,
if you don't have too many classes,
you are able to have labels for
all the classes, then I think
the next question to ask yourself
is what's the domain?
Are you working with 16th century
data on the Spanish empire or
are you working with some data that
you scraped from the web?
If you're working with some data
that you scrape from the web,
you might be able to use generative
AI to do the classification.
And that web data is going to look
kind of like what say GPT or
Gemini was trained on, and
it might work pretty well.
On the other hand, if you're
working with like the, you know,
16th century Spanish data or
something, pretty niche, you know,
you can always try it, but it might
have a more difficult time.
And you know,
the other thing to ask is like how
fine grained and technical is
the distinction you want to make.
And again, if you're trying to make
some very fine grained distinction,
again you might have to kind of
train your own classifier model.
If it's kind
of a general distinction,
you might be able to use GPT.
And so I'm going to talk
about this more and
give you some data in a minute.
I always say like, you know,
why not try GPT, try Gemini,
try Claude, see how it does.
And if it doesn't do well, then you
know that it's cheap to try it.
But let me now
go into classification
in more detail again.
In traditional classification
we have a neural network.
It's mapping our text, let's say we
have text, it's going to map that
text to a series of vectors,
one for each term or token and
the text and then we add
the classifier layer and
it maps those representations for
each of the terms
into our class probabilities.
This is how we traditionally do
classification.
You know, we assign the class to be
the one with the highest score.
If it's like a multi label problem,
maybe we can assign multiple
classes if they're above some
thresholds.
And I'm not going to go into
the technical details of this, but
I have a JL article, I think there
was like a reading list that had it
and there it talks a little bit
more about classification and
what the objective function is.
And really central to the power of
transformer neural networks,
which is the architecture that your
most always going to be using,
at least for the, for
the time being, is the ability to
use the same pre trained language
model as the backbone for a wide
variety of classification tasks.
And so this figure here is
just adapted from the original BERT
paper which was one of the first
transformer large language models.
And so you know, you have those zoo
boxes there, those are the terms in
your text and you're going to feed
those into bert.
And BERT is
a transformer neural network.
You know, it's going to take
those vectors and
pass them through the neural
network, kind of through multiple
layers of the neural network.
And kind of at the end of
the neural network you're going to
get those orange vectors out which
are dense vector representations
for each term in that text that
take into account the context in
which that term appears.
And so if you want to do
classification at the text level,
so like is this newspaper article
about economic policy uncertainty,
what you do is
to just add a classifier layer
to that first token,
which is called the class token.
And that's a token that BERT or
whatever large language model
they'll Have a class token at
the beginning, and that class token
represents the entire text.
You just add your classifier
layer there and it maps to yes or
no, and you choose the one with
the highest probability.
On the other hand,
you might want to classify
the relationship between two texts.
And so, you know,
you might want to say, are these
two texts duplicates of each other?
Are these two texts about
the same topic, et cetera?
And so the way you do this is you
jointly embed them.
So you feed them
into the transformer large language
model at the same time, and
you put what's called a step token,
which is a special token that means
separator.
And the model has seen this in
training and
understands what that means.
So you put the step token between
them and, and again, you know, then
the transformer will do its magic.
It's going to get fed
through the neural network.
And if you want to classify if
they're the same or different,
again, you just put a classifier
layer on that first token,
the class token that represents
the full text in yes or no.
>> Speaker 2: Melissa, this is
a really obvious question, but
when one does that classification,
can one also extract and recover
the probability distribution?
So to get a sense of how certain
the neural network is of whether
this is A or B, as humans,
we have a notion of that, right?
Which of the cases are very
clearly in one bin versus the other
versus which it's very hard to
discriminate.
Can one kind of recover the full
discretized distribution
of probabilities
underlying the classifier?
>> Speaker 1: You could do that,
but it wouldn't really be
meaningful because what that looks
like is going to depend on how you
normalize the neural network.
So at the end of the day,
all that's really meaningful
is which class comes out as most
likely, because that's what it's
trained to do.
And so, you know, suppose you had,
you know, if you had data, say, on,
you know, certainty,
you could like, you know, train,
train a model to distinguish that
specifically or maybe to predict
a continuous number.
But you, you would have to have
kind of the training data and
explicitly train the model
to do that.
And so the, the probabilities
from the classifier, like, yeah,
they're, they're not, they're not,
they're not really, we call them
probabilities, and that's just what
the literature calls them, but
they're not probabilities in
a statistical sense.
The model has just been trained
kind of to put the highest weight
on the most likely class or
to put all the classes that
are positive above Some threshold.
If you change the normalization of
the neural network,
you're going to change what those
class probabilities look like.
If the model is well trained,
it shouldn't change which class is
the most likely.
But you really can't,
unfortunately, can't
interpret them as probabilities.
Calls them class probabilities, but
it's really misleading.
Like, I guess a statistician
wouldn't call them probabilities.
>> Speaker 2: But that seems
important, right. Or
something to be aware of when one's
doing the classifying.
Because it could be that some of
these assignments, you know,
it's actually very hard to
discriminate whether it's yes or
no, and we're doing that, but yet
actually there's not much
information in the raw data.
Right. That seems sort
of important to know.
>> Speaker 1: Yeah, I mean,
I think that, Yeah, I mean, at the.
I think it's
absolutely important to know.
And I'm going to spend the entire
kind of second half of this arguing
that you need to know that you need
to sort of, you need to label data.
You need to know
how well this thing is doing.
But, and you know, you can always
look at places, you know, there is
like a classification boundary and
so you can absolutely pull out
examples that are near
the classification boundary.
Right. And there's
an entire literature on what calls
activation learning.
And it thinks about,
you know, whether that's helpful to
grab things near the classification
boundary and label them and
add them to your training data.
But it's not going to
have a statistical interpretation.
And if you change how the neural
networks normalize, like, you know,
how near things are to your
classification boundary is
going to change.
Thank you.
Yeah.
>> Speaker 3: So I guess adding
on to Steve's question, there's,
there's a literature on handling
survey data where you have to be
careful about reading the responses
of the surveys very carefully and
then doing statistical adjustments
because they're not
exactly classified correctly.
I was wondering if there's
an analogous thing where if I use
a transformer to classify something
when I compute regressions or
statistical estimates on that data,
I have to make some adjustments.
>> Speaker 1: Yeah.
So after lunch I'm going to talk
entirely about that.
So that's absolutely the right
question and I'm going to argue
that you need to do that.
And so, yeah, like I'm going to
spend the entire time after lunch,
or however much time we have to
devote to that part, arguing that
that is super important.
And we do actually cite
that literature,
like some of the seminal work by
Angus Deaton in that literature.
I mean, it's still it absolutely
applies to neural networks.
All right.
And so
kind of the third type of problem
you might want to do is you might
want to make predictions about
individual terms in your text.
And so one classic example of this
is called named entity recognition.
So let's say we want to recognize
every person
that is mentioned in the text.
And so if the term the token
refers to a person's name,
we want to tag this person and
like, specifically begin person
and, you know, the inner person.
And so we want to tag that.
And then everything else
would be other, right?
Or, you know,
we might want to tag locations,
organizations, firms,
kind of whatever.
Kind of, you know,
whatever you can dream up.
Universities, the list
goes on and on.
I want to tag in a biography,
who's the mother and
who's the father.
Anyways, the point is,
I want to tag.
I want to tag individual terms
based on what information
they contain.
So that's called a named entity
recognition problem.
And there you just put separate
classifier heads on
each of the token vectors that come
out of the transformer.
And so that's in panel C. Or
I might want to recognize
spans of text.
Like, there's a question and
a paragraph, and I want to say,
where's the answer
to this question in that paragraph?
And then again, you're going to.
You're going to do classifications
on the individual tokens.
And so the general point of this
is, what's so powerful is before
Bert, like before Transformers,
each of these problems would have
a different architecture, like,
totally different way of
solving them.
But now, like Transformers,
you can just do anything.
Like, you basically, you get these
vector representations, and then
you do whatever you want with them,
whether it's classifying the text
or similarities between text
on the class token, whether it's
classified individual terms.
And that makes Transformers
incredibly powerful.
And I know I haven't talked about
what Transformers is like, so I'm
just going to leave this as a black
box, but there's really amazing
tutorials out there explaining
Transformers and how they work.
So if y' all aren't familiar, like,
there's links to that in
the knowledge base, and
there's just videos that do
a phenomenal job of explaining it.
All right, so
classification kind of in the sense
that we've been talking about,
where you add a classifier layer,
that's a supervised task.
And so the model must see a
sufficient number of examples from
each class during training in order
to perform well on unlabeled data.
So if you want to classify.
Is this newspaper article
about geopolitical risk, yes or no?
You have to give it enough yeses
and enough nos in training that it
learns to recognize that
an alternative approach is that you
can use generative AI for classes.
And so you have a prompt and
you explain to GPT, you know,
I would like to classify whether or
not this article is about
geopolitical Risk.
My definition of geopolitical risk
is, you know, this yes or no.
You know, GPT other models, they
have structured outputs so you can
actually force it also to return,
you know, a yes or no answer.
And so in a JL article that I have
on deep learning for 19 different
topic classification tasks, all
using historical newspaper articles
from the us, we compared GPT
to our own custom trained model.
And I think the bottom line is that
the custom trained models
are almost always more accurate.
But like sometimes GPT is really
good and you can just use that.
So people ask all the time,
can I use it or not?
And my answer is always,
why don't you just try it?
Because it's cheap and
easy to try it.
And so yeah,
in this case we're comparing 3.3.5
to I think to 4.0 or maybe 4 turbo.
In the time that
it took to write this article and
get it published, OpenAI made a lot
of updates to GPT.
There was a big improvement between
3.5 and 4.
After that, not so much.
I haven't tried 5 yet
on these topics, but
I will do that.
But I have to say we're still
classifying things and using it.
And I think the bottom line is
sometimes it works great and
sometimes it doesn't and it's
always a little hard to predict.
So Sendhil and Ashesh and
others have an ENT kind of
fantastic research agenda on
how AI makes is very non human and
the mistakes it makes.
And so sometimes it can do a hard
task, but it can do an easy task.
And they've done kind of
experiments where they show humans
are really bad at predicting what
it's good at and what it's bad at
because it just, it's not.
A human doesn't behave like we do.
And so
I always say like just try it out.
But you can see here
kind of the pattern that emerges.
And I'll also say that GPT trained
means we took a Roberta model,
which is an open
source large language model and we
just trained it on the GPT labels.
And the bottom line there
is if GPT is not very good, that
does terrible because the model is
learning from bad data.
But if GPT is doing really well,
then that also does really well.
And the reason why that's relevant
is say you have 50 million things
that you want to classify.
You're not going to be able to
afford to do that with GPT or
Gemini or
whatever your preferred model is.
You're going to have to
do it yourself.
But if GPT
can Do the task perfectly.
You can use the GPT labels
to train.
I think the bottom line here is
things that are really
straightforward is this article
about antitrust.
GPT understands what antitrust is
and it does really well.
But there's other things where it
just does much more poorly.
Even like, you know,
say something like crime.
I guess crime is just like a pretty
diverse category.
Doesn't exactly understand
what we mean, even when we play
a lot with the prompt.
I guess I should say
another thing here that's extremely
important is you want to know how
well GPT is doing.
And so when you engineer your
prompt, do that on a separate
set of data from your test set.
Because if you're engineering your
prompt on your test set,
you're just overfitting
the prompt to your test set.
And we have no idea
how it does on unlabeled data.
And so, you know, there's
a lot of things to go through here.
You know, polio vaccine,
that's really obvious.
So it does really well, you know,
but some things, you know,
is this a schedule?
Is this about sports?
Those are all really, like,
pretty straightforward horoscopes,
is very straightforward obituaries.
But there's some things, like,
I think it's interesting, like it
does way better on the Vietnam War
than on World War I.
And I think there's two reasons for
that, that, like, there's just more
about the Vietnam War on the
Internet and its training corpus.
And so it just
understands that better.
And, you know, the English language
has not changed so
much in the past hundred years
compared to some other languages,
but it's changed a little bit.
And sometimes that can just like
throw a large language model for
a loop, you know, even though it's
pretty clear to a human.
So it does actually pretty poorly
on World War I Articles about
World War I, but much better
when it comes to Vietnam.
>> Speaker 2: Have you tried to see
what happens if you take an open
weights frontier model and
you train it even
lightly on these categories?
Suppose we
take an open weights model and
you do some training yourself
on predicting these categories.
Would that do really well?
Because it gets rid of some of
the simple mistakes.
>> Speaker 1: So that's essentially
what I'm doing in
the columns 4 and 5.
And so distil Roberta is an open
model with about 80 million
parameters.
And Roberta Large is like,
I think 320 million.
And so I'm training those
on kind of on labels, essentially.
And yeah, I think the bottom line
is it tends to, like, almost always
do better, but sometimes
that better is very marginal.
If GPT is pretty good.
We also tried Claude.
We had a big problem with Claude.
So Claude has this,
like, constitutional AI framework,
and they're really into AI safety.
And so it kept on telling me that
I was feeding it toxic content.
And sometimes you could understand
why, but sometimes I didn't
even understand why.
It was just like an article.
It's about World War I,
and I guess it's.
Kind of talking about violence, but
nothing you would see as offensive
anyways.
Like, yeah, we've never had GPT
refuse to do something for us,
whereas we had a lot
of problems with quad saying that
whatever we feed it is toxic.
Sometimes I did feel like I need to
explain to GPT, I'm a researcher
studying historically, don't want
to get thrown off the platform for
feeding it, like, you know,
op EDS from Hitler or something,
which did exist.
All right?
And so again, I said,
the bottom line is try.
The other thing that can maybe
be a downside is
that models get deprecated and
disappear all the time.
You know, so you might hear on
the news where people
are really sad because they have,
like, companionship with 4.0, and
then it disappears.
I guess the equivalent of that for
us as researchers is like,
I can't reproduce my findings.
And so that's why,
like, it's always an alternative.
Let's say you want to classify
whether something's an obituary.
And GPT can do that perfectly.
But you can also just have GPT do
that perfectly for,
like, a thousand examples.
Train your own classifier,
which will also be perfect.
And then you
always have that model.
And so you don't have to
deal with a data editor being like,
what's going on?
Like, why can't you be able
to reproduce your findings?
And so that's, you know,
it takes training.
A classifier is the task that I
always have my undergrad already
start with, so it's not completely
trivial, but it's, like, about as
straightforward as things can be.
And so, like, you know, if you
don't want to take the risk of,
like, people complaining that you
can't reproduce your results
because you did them with 4o and
now 4.0 is gone.
You know, there's always
the option, you know, at least for
things that are relative, like,
straightforward classification.
I mean, I know with this article,
it was in the jl, so it was the AA
data editor, and they're like,
yeah, like, we're okay
with you using an OpenAI model.
Obviously, it was. The point of
this table was to use it.
But they're like,
we're okay with that.
Like, even if it can't be
reproduced, as long as you specify
exactly what you did.
So I think that's kind of in flux,
like, how we feel
as a profession about the fact that
these models are a concept
suddenly disappearing.
But that is one
caveat to keep in mind.
All right, so
that is classification.
And hopefully, you know that
that's all pretty Straightforward.
And again, there's more kind of
technical details.
There's notebooks that you can use
to train your own classifier,
like on the Econ DL website.
I don't think I've referred to that
yet in the slides,
but I will in a little bit.
All right, so now I want to move to
talking about embedding models.
And again, I'm not going to
go into the technical details, but
I'm going to give you
lots of examples, and I'm going to
talk about three different cases
where it makes sense to use these.
The first case, you don't know
what the classes in your data are.
You essentially want
to explore your data.
You want to make sense of your
data by dividing it into different
groups or different classes, but
you don't know ex ante
what they are.
The second type of application is
that you have a lot of class, and
it's just computationally unwieldy
to train a classifier.
And then the third
type of problem is you want to add
classes at inference time.
So when we say inference,
in machine learning,
inference is running your model.
Okay, Again, it doesn't mean
the same thing as inference and
statistics, so
I know it gets confusing.
So when we say we want to
add something at inference time, it
means you've already trained your
model, and then you want to add
new classes when you run the model.
And you can't do that with
a classifier because
the model hasn't learned
the weights to map into that class.
But you can do that
with embeddings.
And there's lots of cases,
like, you know, where we would,
like, want to do this.
So one example,
let's say you're working with
historical banking data and
you have your own customized ocr.
And then you realize, like, there's
this little telephone symbol, and
it splits this and this, and
I need that, or
the OCR doesn't make sense.
Well, there's not like a telephone
symbol in your ocr.
You don't want to go back and
retrain the mod
with an embedding model.
You can just add it
at inference time.
And so we'll talk a little bit more
about that as well.
All right.
And so again, just to refresh,
embeddings are the dense vectors
produced by a deep neural network.
And so if you have a text, there's
going to be an embedding for
each token in the text.
You can think of tokens as,
like, words, although sometimes
they're subwords if the word isn't
in the dictionary.
But think about it like words
for your text,
you have this continuous vector for
each word in your text,
as well as an overall vector that
represents the full text.
Or if you're working with a vision
transformer for each patch,
which is kind of like an adjacent
group of pixels in the image,
again you have a continuous vector
representation of that patch
of the image.
So we're going to be talking now
about working directly
with those vectors.
The first thing that I'll say is
you generally do not want to work
with the embeddings of off
the shelf transformer models.
So that would be like bert,
Roberta, you know, GPT is it just
off the shelf transformer models.
And the reason for
that is they have some undesirable
geometric properties.
They're anisotropic.
I don't want to go into
the technical details of that.
But essentially the space created
by say a BERT transformer,
it's not a convex space.
And so it's going to be problematic
when you start working with those
vectors because essentially
the model hasn't been trained to
work with the vectors and there's
holes in the space and whatnot.
And so there's a big
literature on this.
But the key thing
to know is that there's a method
called contrastive training that
can be used to make the distances
between the embeddings and
the vector space space that's
created by your neural network
meaningful for your problem.
All right, so the basic idea of
contrastive learning
is that you're learning a mapping
from your unstructured data, so
your text or images to a continuous
vector space, just like you would
with any transformer model.
But now you're training the model
such that instances that belong to
the same class
have similar embeddings, and
instances that belong to different
classes have dissimilar embeddings.
And so it doesn't have to
be like a discrete class problem.
You could train it
on a continuous distance, but
oftentimes we don't have that.
So oftentimes what we're doing with
contrastive learning is okay, we're
training the model to say, okay, if
these two vectors refer to the same
person, put them close together,
if they refer to different people.
So let's say it's two different
John Kennedys,
not the same John Kennedy.
Put these vectors further apart
above a threshold distance.
I mean, I'm going to show lots of
examples of models that were
contrastively trained.
And that makes these kind of
distances between the vectors
meaningful for grouping data into
groups of like things.
And so all the technical details
about contrastive learning
are in this knowledge base.
All right, the first thing I want
to say is, you might wonder, can I
just use embeddings off the shelf,
or do I have to tune it myself?
Because from OpenAI, for instance,
you can go and buy embeddings, and
they're actually very cheap.
And so OpenAI will sell you.
I don't think they sell you for
the individual terms.
But they'll sell you the embedding
for your full kind of text
that you put in.
And so you might say, well, can I
just use the off the shelf ones?
And I think in this case the answer
is kind of almost always no,
because your vector representation
of your text that contains
a lot of information in it,
information about the syntax,
the semantics, the topics.
But maybe all you care about
is the topics, right?
All.
And you want to tell the model that
by giving it some training data
where you make those vectors closer
if it's on the same topic and
further if it's on different
topics.
And if you don't do that,
the model doesn't know that you're
interested in the topics.
Maybe more pulls out like, okay,
these two have similar syntax, but
that's not what you're
interested in.
And so I want to give
an example of this that comes from
the comparative agendas data set.
This is a data set, you can
go download it online, which
is why we used it for this example.
And it has really high quality
topic tags about legislative acts.
So think about this
as bills in Congress, you know,
acts of parliament, etc.
And it divides them into different
detailed classes.
And so
we can use off the shelf embedding.
So probably the most well known
off the shelf contrastively trained
embedding model that's open source
is called sentence bert and we use
sentence Bert a ton in my research.
It's open source, it's super easy.
They have it for many
different languages, they have it
trained on different things.
It's a really useful resource.
And so we look at the sentence BERT
off the shelf embeddings, meaning
we haven't trained them at all.
We look at OpenAI
off the shelf embeddings,
we just take them from OpenAI,
we don't do anything with them.
We just say, do these group like
topics together?
And the answer is not very well.
But if we train on a limited amount
of data, so
even just hundreds of pairs going
to thousands of pairs of data, it
starts to do a much better job.
And I want to show you that
with some figures.
So this is Sinson's bird embeddings
off the shelves and
you see the cosine similarity.
So a measure of how similar
embeddings are within topics and
across topics.
And like with cosine similarity,
the smaller it is,
the more similar they are.
It's like the angle between these
two vectors.
And so you can see in blue that
embeddings in the same topic, they
are more similar than embeddings
across topic, but there's a lot of
overlap in that distribution.
So you're going to have a hard time
taking these embeddings,
clustering them and
pulling out coherent topics because
there's just too much overlap.
And that's because these embeddings
also think about the syntax and
everything else that's in the text
and not just the topic and it looks
basically exactly the same.
With OpenAI, it doesn't really
matter if you use a larger model,
it still doesn't understand that
what you care about is a topic.
But here we fine tuned and you can
see you get much better separation.
It's still not perfect.
And basically if you look at
this overlap,
it's because like this data set
assigns every bill, you know,
every act of Congress one topic,
but some of them are multi topic.
And so most of the cases of
overlap are like genuine.
You know, this is actually about
two topics and
the label is not perfect.
So it does much better.
We can take this model trained on
US bills, take it
to acts of Parliament in the UK and
it still does like reasonably well.
And so there's some amount of
transfer learning
that's possible there.
But the bottom line of this is just
you might need to tune
your own data.
Fortunately, one of the really
powerful things about contrastive
learning is that it's
extremely sample efficient.
And so sample efficient means you
don't need to see
a lot of training examples
compared to some other much more
complicated architectures,
much more complicated models that
are out there.
And so if this is kind of abstract,
what I want to do now is to give
you a bunch of different examples
of how we've used embedding models,
contrastively trained embedding
models to measure things that
can perform tasks that are relevant
to economists.
Okay, so the first thing I wanted
to talk about
is detecting reproduced content.
And so in this case we have some
noisy data.
It could be data from the Internet,
which is like the clean
corpus of the Internet.
That essentially is what large
language models
are trained in large part on.
It could be historical
newspaper articles.
We've looked at both
of these examples and so I was
from a social science perspective,
I'm really interested in historical
newspaper articles.
Historically in the US about half
of content in local newspapers came
from a wire, like a news wire.
The most common one
is the Associated Press.
But the articles,
they won't be exactly the same.
Local papers abridged them so
it will fit on the page.
There's also OCR errors and
actually there were kind of
different versions that came
from the Associated Press.
We call this choose your own
adventure because they
put the controversial things at
the end of the article and
then say may insert after line two,
may insert after line seven.
And you could choose what politics
I think the article conveyed by
choosing to insert those things.
And so
they're not exactly the same, but
they're pretty similar.
And so that's one application.
I also have some work with other
computer scientists where basically
what we found is OpenAI did not
adequately deduplicate their
training data with the test data,
with the benchmarks that it's
evaluated on.
And when you look at
how GPT3 performs,
it did much better on benchmarks
that they did not get out
of their training data because they
were just using 13 gram overlap.
If there was a 13 gram overlap,
they took it out.
But the Internet's noisy.
There's lots of small differences
in punctuation or whatnot.
And so this issue really,
like noisy duplicates,
really influences how we interpret
how well large language models do.
Because if you don't deduplicate
the test data out of your
training data, then it's
like cheating essentially.
But I'll talk about
reproduced content since that's
maybe more intersect
interesting to us as economists.
And so we developed novel methods
where essentially we trained
a model on labeled data to say does
this article come from the same
newswire source or
a different source?
So we contrastively train that
starting with an SBIRT based model.
And then we cluster and
we use single linkage clustering
because that's incredibly scalable.
Things like hierarchical
agglomerative clustering won't
scale the large problems, but
single linkage will.
We do community detection, which
helps to break some of the false
links from single linkage since
it's kind of the most scalable but
not always the most
accurate method.
And so we do that.
We embed a massive number
of newspaper articles and
then if it's in the same cluster,
then we say it comes from
the same newswire source.
So this is very accurate.
This is reporting here the adjusted
RAND index,
which ranges between 0 and 100.
It's probably the most commonly
used measure of clustering.
Like how well is your clustering
doing when we compare it,
when we compare it to the non
neural method.
So just looking for, you know,
N grams, common N grams, or
hashing, which is a computationally
efficient way of looking for
common engram overlap, it does much
better to use this neural method,
you know, because small differences
can break looking for
exact term overlap, but then neural
network can account for that.
You know and you know I won't make
the distinction between line.
The first and second lines,
essentially we just have like
an extra step that can
increase accuracy but
also makes it less scalable.
And so I want to talk about
what did we do with this model?
We released a data set called
the Newswire data set.
And we start with about 138 million
front page articles from historical
local US newspapers spanning
a hundred year period.
And we find kind of using this
model that There is about 99 unique
articles, including singletons.
About 2.8 million of those
are reproduced more than four times
or more than three times.
And then we kind of reduce to
wire articles,
get rid of syndicated content.
And this data set is all
available on Hugging Face.
And so if you're interested in
these historical Newswire articles,
you can go and just download this
data set and use it.
There are OCR errors.
You know, we're slowly cleaning
this on GPT, but we just use the 10
million free tokens we get a day.
10 million
tokens might sound like a lot, but
we calculated it would take like
180 years or something to clean.
All unique 99.4 million.
But you know, if
you want to use it a subset of it,
you can also clean it.
We include other information.
So we extract
again with deep learning,
we extract the date line which is
where the article was published.
You see articles coming from across
the us
this is international datelines.
I mean you can clearly see wars
in this figure.
So it all kind of, it makes sense.
We have topic classification models
and I think
that this is pretty interesting.
Like say on crime, you know,
you can see the prohibition spike,
on protests, you see the 1960s,
these are high quality kind of
topic classifiers that we trained
ourselves with our own label data.
We also use topic tags for,
from the comparative agendas which
are maybe not quite as high quality
but kind of give us more topics and
those are available as well.
All right. Another
thing that we did related is so
local newspapers, they got their
articles from the Wire, but
the Wire didn't give headlines.
Their editors
wrote their own headlines.
And this is pretty cool
because it gives us a human made
data set that's different
ways kind of to say the same thing.
And so we released all these kind
of pairs of headlines that
appear here.
And so you can see that there's
just kind of, you know, a massive
number of paired headline data
that are kind of two headlines for
the same article
saying different things.
This is really interesting from
an ML perspective because
it's great for training semantic
similarity models, but also
from a social science perspective,
I mean, you know, sometimes it's,
you know, they just wrote
a different headline, but sometimes
you can clearly see the politics
and kind of the different
interpretations of the same thing
in it, which is pretty interesting.
Again, it's all on hugging face.
All right, the final thing I want
to say is that this
model is incredibly computationally
efficient.
So this is for a paper we did.
We looked at de duplicating
10 million articles.
Most of the time is to embed it.
This is just on a single GPU card,
but we can do the 10 to the 14
vector calculations in
about three hours on a single card.
So once you're in a world where
your data is in dense vectors,
it's just you can do things at
an insane, like unbelievably insane
scale very cheaply.
It's not a fancy GPU card
or anything.
We bought it in 2020.
There's four cards on the machine.
It wasn't that expensive.
And so this is a card that like
my students can get with their very
limited research budgets.
All right, if you
also thought about.
>> Speaker 2: Using the sort of GPT
as a kind of sort of
creative tool to design research
questions or in some sense.
So now you've got these newspapers
that have been digitized in the
archive, you can start to imagine
what statistics locally reflected.
You know, how should I classify
these data in order to capture some
local variation that's not captured
in official statistics?
So kind of sort of a higher order
reasoning or sort of use the model
itself to guide the research.
Question, does that make sense or
is that meaningless?
Or you think this is the scope to
do that?
>> Speaker 1: I mean, I think part
of the challenge would be like
the scale of the problem, you know,
so we have like in total
like over a billion articles,
like and yeah, we can de.
Duplicate them and
then that like cuts down.
But there's just like so
much content like, and it's not
like you could put all that content
into a prompt and Yeah, I mean, so
I think it's like, I think it's
an interesting idea, but you'll see
kind of other ways that we've tried
to make sense of what is in this
data, which is what my other
examples are going to show you too.
But like none of this uses GPT
because I think you kind of need it
to be customizing the scale would
just be completely infeasible.
Even using many which is
the cheapest, it would just be
very, very expensive.
Whereas with a much lighter custom
train model on our own machine,
we can run it really easily.
But obviously
there's things you can't do.
But going exactly to that point,
one thing we wanted to say, okay,
is what was the biggest new story
of the year?
We have no idea.
X and Z, so
we can't build a classifier.
And so what we did instead
was to take data from this website,
all sides, and from modern news
articles, it will collect, like,
say, here's these five different
articles about the same story.
One's from Fox,
one's from the New York Times,
one's from cnn.
And so
we use that to train a customized
model, just starting with the wire
cluster model as the base and
then tuning it to put things that
are about the same story from this
all sides data close together and
things that are about different
stor further apart.
And then we cluster the resulting
embeddings.
And this is.
We did this on the American Stories
data set.
This is 20 million newspaper scans
that we Digitized from
Chronicling America collection.
And so we apply it to these data.
And these are the biggest stories
for each year.
I think it's pretty interesting,
as an economist,
that a lot of these stories
are about economics and specific
specifically about labor issues.
Like, you see lots of stuff in here
about strikes, obviously.
You also see a lot
of stuff about conflicts.
And then there's
really random stuff.
1909, race to the North Pole.
So there were these two guys who
were racing to get to
the North Pole first, and they had
a big fight who got there first.
And it was just like coverage of
this fight for an extended period,
I guess not much else was happening
in 1909.
So sometimes you get random things,
but mostly it's.
It's pretty interesting.
And economic issues, like,
certainly matter.
So for labor historians,
there's a lot of material.
Okay. A final version of this,
which was just essentially like,
for fun, is we took that model.
We mask out named entities which
are essentially like proper nouns,
like locations, organizations,
individuals.
And then we say, okay,
for a modern news article, what's
the closest historical article?
And.
You see an example here.
Mostly this just
provided us with entertainment.
Again, the model is like online.
I'd like to build out a better
version of this where you can put
your own article in, but
that takes money that I just don't
have lying around at the time.
But it's really fun to play with.
I mean, maybe it's interesting to
people here.
We pulled out various articles.
I'm convinced people in the 50s
thought that AI as we have it now
would exist by 1965 or
something like that.
They really did.
So it's interesting for
thinking about optimism in tech,
but we had a lot of fun with campus
protests and university issues
because it all goes to the 1960s.
And you see the same things like,
if you don't get these protesters
off the Berkeley campus, we're
defunding Berkeley and suspending
all federal research funding.
But they didn't actually do it.
Nixon didn't do it,
but he had the idea.
All right, and
then I'll finally say you can do
the same thing with images.
And so this is just the same idea
where we have in here,
this is mostly trained on synthetic
data because you can
synthetically like crop and
noise images and we can figure out
what's the most reproduced
newspaper images in a given year.
Again, you know,
you have this custom trained model,
you map all the images to
vectors and then you just cluster.
So not surprisingly,
like the most reproduced image of
1969 was the Moon landing.
You know, just a sanity check.
The most reproduced one of 1967.
I'm just showing you
some fun examples here.
I guess it doesn't really have
a point, but people love showing
like violence in progress.
This is a case where
this guy was standing trial and
he smuggles in a gun and
takes the courtroom hostage.
And they got a picture of it.
So that was the most
reproduced image of 1970.
Obsessed with plane crashes, people
ask about women in the press.
And so
almost all the pictures are of men.
I had a student who was labeling
images for this and she's like,
I've been labeling all day.
There's only one woman and it
had her waist size in the caption.
It was like, probably homecoming
queens are the most common thing.
But we did find these
popular images.
Jackie Kennedy, of course,
the Manson murderers.
There were these nice looking women
who were in a cold and murdered
people, but not a lot of women.
This is just in case you fell
asleep during the other stuff.
May, this is entertaining.
I mean, a more serious thing that
we wanted to look at is
there's all These news articles
about images that change history.
People talk a lot
about the napalm girl image.
Okay, so I'm going to show
that image.
Hopefully it's not
too disturbing to anybody.
This is an image of children
in Vietnam being burned by napalm.
There's another famous one of this
Viet Cong
soldier who's about to be executed.
And there's a lot of people who say
this changed history.
This made Americans realize that
we should get out of Vietnam.
And so we're like,
well, is that true?
We found that the image was not
very widely reproduced.
It did run below the fold in
the New York Times, but people
didn't like the frontal nudity.
We find no impact on abnormal stock
returns of Vietnam War contractors.
There's a minimal but very small
and short lived abnormal return of
Dow Chemicals who made napalm.
If you look at
mentions of the napalm grove photo,
they take off only after the woman
who's in this started
a public charity in the 1990s.
So I think this is
pretty interesting.
It's kind of.
And you see this mentioned a lot
today when something
relevant comes up.
The drowned Syrian refugee toddler
and Angela Merkel mentions that.
And then people start
talking about napalm girl and
how images can change things.
And it's more like we filter
the past through the present.
And when you can go and
actually see the past as they saw
it at the time through newspapers,
it can look very different than how
we remember it.
All right, so
I want to shift gears.
Like all the examples I've showed
you so
far are about, you know, about
cases where we kind of essentially
want to explore the data.
We don't know what's in there.
Another reason we might want to use
embeddings is because we have a lot
of classes.
So let's say you want to merge
the 1930 and the 1940 U.S.
census and there's millions of
individuals, you want to, you know,
merge firm databases.
You just, you have a lot of
different classes in them.
And so
record linkage is fundamental.
You know,
anytime you might need to link,
you know, individuals, firms,
products, you know, relatedly,
you might need to aggregate,
you know, products into industries,
et cetera.
These are very,
very common kind of data challenges
that we face before we can do
the analysis that we care about.
And it turns out that deep learning
is really powerful for them.
And so traditionally we link
records with string similarity.
The problem is string similarity
doesn't understand semantic
similarity, co incorporation,
they mean the same thing.
We know that, but
they're very different strings.
And so what I did is work with
a student, Abhishek Arora, to build
a package called Link Transformer
that aims to make it easy to use
large language models for
tasks like merging,
de duplication, clustering.
And so
it supports standard merging,
merging with blocking or
multiple keys.
One thing that I think is kind of
fun is you can bypass translation
by using a multilingual large
language model to link across
different languages, which is
a domain where traditional record
linkage with strings is terrible.
You can use it for aggregation.
So say, aggregating products into
industries.
We also allow you to train your own
classifier with it and it supports
any model in the hugging face hub.
Or you can just directly use OpenAI
embeddings.
And we have our own models that we
train for six different languages
for different types of tasks.
So mostly like linking firms,
linking products, aggregating
products into industries.
You can go see the paper and
see how well it does, but
just the punchline is it does way
better then string matching.
And usually your customized thing
does better than
using OpenAI embeddings.
But OpenAI embeddings can be
decent if you're doing
something pretty simple.
And they're very easy to use.
The idea here is, let's say we have
a bunch of firm names, we have
some link transformer model.
We use that to map those firm names
into vectors.
Then once we have vectors, we can
compute distances between them.
And that's a distance, just like at
a distance is a distance.
And you can use these vectors in
the same used at a distance.
But unlike string distance,
these distances account for
semantic similarity.
We try to design the package so
that it's familiar to people coming
from environments like R or Stata.
Like this is in Python, you would
not be able to do this in R.
But we try to make it intuitive.
We try to make it intuitive to
train your own model.
So the basic functionality is, you
know, we have lists of firms and
we want to merge them together.
You do that with a simple line
of code.
As I said, really
I have like abandoned projects
because I'm like, I cannot link.
I can't link products
across two languages unless I do it
all by hand.
But now multilingual language
models make that easy.
Here's deduplication again,
kind of same principle,
aggregating products, industries.
I mean there's always some
ambiguity in which products go into
which industries.
But we use like data from the unit.
On product classifications.
And we evaluated this on historical
data, you know, before you had
those UN classifications.
And it does pretty well.
One of our motivations was
studying the impacts of import
substitution industrialization.
We have these tariff schedules and
every month they like change the
name of the products and you need
to be able to link them together.
And this was before
harmonized data.
So there are no codes.
You just have the description of
the product, its name and
the tariff.
And we were able to get really
high accuracy literacy using this
model for those products.
It's pretty
straightforward to train a model.
Okay, so that's using large
language models for record linkage.
You know, I'm probably
overwhelming you with examples, but
I want to say you can also use
vision for record linkage.
This would probably be
unnecessary if you're working, say,
in a Western language.
But it's super useful, I think,
when working with, say,
traditional Chinese,
Japanese character based languages,
because OCR is still,
still not as good the vast majority
of the time as we wish it were.
And you can account for the fact
that you can account for the visual
similarity between characters.
So again, I work with
a group of students.
We contrastively trained a model
on digital fonts to measure
character similarity.
So basically we used a bunch of
digital fonts and taught the model
characters, the same character in
different fonts give those similar
vector representations.
But it turns out that this actually
works pretty well across fonts.
As you can see here,
an example character, and
then you look at the most similar
character and we've done this for
different Asian languages.
And you can see it kind of tells
us pretty well which
characters are visually similar.
And then that allows us a very
cheap way to do kind of better
merging that accounts not just are
these the same character or not,
but it accounts for the similarity.
And because oftentimes,
like, let's say names in Japanese,
they're like three characters long.
If you get one of those
characters wrong,
you are not merging your person.
Like you just lost
too much information.
But when you take into account
the visual similarity and
the types of errors that are likely
to be made in digitization,
it makes it much better.
We had fun applying this to ancient
Chinese from I think like 1300 BC.
And so these are ancient
characters, what the ancient
character meant and the modern
character that descended from them.
And it's just really interesting
because the characters that the
model said were visually similar,
like archaeologists say that these
have similar abstract meanings.
And so kind of these ancient people
when they drew a picture for like
more abstract things, like things
that had kind of Similar meanings.
They drew more similar pictures.
So, again,
I'm not sure this has any economic
application, but it was easy for
us to do this, and it was fun.
All right, the final thing you can
do is say, I want to use both
the language model and vision.
And so we did this
in a paper called Clippings.
It's a multimodal model.
I don't want to go
into the details of how we did
this because it's pretty technical.
And I think, like,
working with a model like this does
get pretty technical.
When you're working with
kind of multiple modalities,
it becomes more involved.
But basically,
we were trying to link Japanese
firms across time, and
we wanted to use both the visual
appearance of the characters, but
one of the documents was written
horizontally and one was written
vertically so that we could account
for problems with the OCR and
very similar characters.
But we also wanted to use
the semantics because you write
firm names differently, but
they mean the same thing.
When we took them both
into account,
we got almost perfect merging.
Whereas using just language or
just vision was like, okay, but,
like, not as good.
You know, One of the things that we
were interested in this Japanese
data for was to look at antitrust
policy that the U.S. implemented in
Japan after World War II.
They came in, they tried to break
up a lot of large Japanese firms,
but the Japanese had various
ways to get around this.
And so when you look at input
output networks in 1957, which is
a few years after the US left, and
you look at the big firms that they
tried to break up, which are the
kind of colored dots there, they're
still the most central firms in
Japanese input output network.
And so basically,
like, we would have never been able
to kind of link firms together in
the multiple sources.
We needed to put together kind
of full input output linkages.
If we hadn't been able to use
deep learning for record linkage, I
think it would have been helpless.
All right, I want to give one more
example of record linkage, and
I think this is really cool.
And so I've been talking so
far about kind of traditional,
you know, merging.
You know, we have
two data sets that firms appear in,
and we are individuals, and
we need to merge them.
But another kind of merging task
is with unstructured texts.
And so we have these historical
newspapers.
You know, I was asked before,
how do you explore what's in them?
Well, you know, these men,
there's like, you know, billions of
mentions of people in particular,
and we'd like to understand
who is the newspaper talking about?
And so what we'd like to do is
we've already done named
entity recognition to
tackle the individuals.
And then we want to say, does this
individual appear in Wikipedia?
And if so, who are they?
What we do
is to contrastively train a model.
And we did this on
the Wikipedia disambiguation pages,
which are pages that list, say,
all the John Kennedys that appear
in Wikipedia.
That gave us literally billions of
pairs of training data for free.
We didn't have to
label our own data.
We could get that from Wikipedia.
And then we embed the mention of
the person in the newspaper
article, all the first paragraphs
about Wikipedia.
And, you know, we tune it a little
bit on some label data so
that the model, you know, if it's
President John Kennedy, it puts it
close to the John Kennedy page.
If it's like local councilman
John Kennedy, it's far away from
everything in Wikipedia.
And we say,
this person is not in Wikipedia.
And I think this is impressive
because there's like
millions of people on Wikipedia.
There's even more people,
like in our newspapers.
Just a sanity check,
who are the most mentioned people?
Label is pretty
much what you would expect.
Hitler, Eisenhower, Nixon.
I think it gets interesting when
you think about who was
mentioned historically, but
is not in Wikipedia.
And so the most commonly
mentioned person
historically in our newspapers that
doesn't have their own Wikipedia
page was the guy who was manning
the phone lines at Pearl harbor
when Pearl harbor got bombed.
And so basically he gets called,
and the guys with the scopes
looking are frantically being like,
the Japanese are coming.
You've got to move the fleet.
Like, and
this guy was manning the phone.
So he told his boss, and
his boss was like, whatever, like.
And he just didn't care.
Ignored him.
I'm doing something else right now,
you know, and they're just calling
him frantically.
And the guy thinks about, you know,
should I go, you know, should I go
over my commanding officer and
tell someone else?
But in the end, he doesn't.
And then Pearl harbor gets bond.
But I guess we
don't like to remember that.
Like, I never knew that, like,
you know, Pearl harbor got bombed
because the Americans were really
incompetent versus, like,
the Japanese were this amazing
force who we then defeated.
It's not like it goes back to
how we tell history
versus what actually happened.
But anyways, you can imagine a lot
of different applications of being
able to do something like this,
because once you get to Wikipedia,
you have Wikidata.
There's tons of
structured information there.
And then you can kind of.
There's a lot that you can do.
And so this was essentially, again,
this is using embeddings, vector
representation of the mention of
that person in the article and
the context around them.
A vector representation of
the Wikipedia text.
And with that you can figure out
with like reasonable accuracy and
you can go see the paper who's who.
You know, there's other methods and
we compared all of those
in the paper.
An advantage of this method, again,
when you're working with these
vector representations, it's just
insanely computationally efficient.
And so, you know, as social
scientists, it doesn't matter like
we're never going to have that
great of a compute budget compared
to like OpenAI or whatever.
So we have to think about, think
about computational efficiency.
All right, a final application,
adding classes at inference time.
And I'm going to talk about this in
the context of ocr.
There were other reasons we wanted
to design our own customized OCR
architecture.
The traditional architecture used
by OCR is a joint vision and
language model.
And it's very simple and
efficient to train.
And so
we had these Japanese documents.
The best OCR available anywhere was
Baidu.
And it got like over
half of the characters wrong,
which is not going to cut it.
We needed to
design our own customized ocr, but
we would never have enough training
data to tune this complicated
language vision model.
And so what we did
was essentially to treat OCR
as an embedding problem.
I'm showing this here in Japanese,
but we also did this for English.
And our newspapers are digitized
with our model for English.
And so we recognize kind of
individual characters or wor and
in Asian language characters r
words and we embed those
with a vision model and then we
just compute the nearest character
in a digital font that we've
also embedded with the same model.
And that's how it's transcribed.
And this compares to the bottom
row, which is
traditional OCR architecture.
It's an architecture
called sequence.
To sequence, you're not recognizing
individual words or characters,
you're dividing it into patches.
And then it's very complicated
because you have a vision and
a language model and
you have to jointly tune those.
And that's really computationally
efficient just using vision.
It works really well.
It's super sample efficient.
And so those top two lines on
the left are an open source
transformer model that Microsoft
trained on 670 million images.
And you see, it just does nothing.
It doesn't get any more accurate
when we train
that architecture on our data.
Whereas ours, which is the orange,
it learns very efficiently.
Again, you know,
if you're digitizing English
typewritten stuff, just use GPT.
Okay. It's amazing actually.
And it can
like pull out stuff and it's great.
I think it's really transformed
a lot of stuff that I have to ocr.
But if anybody here is working
with, you know, weird stuff,
you know, old handwriting,
Asian languages,
we have this custom OCR package.
We try to make it super friendly.
There's a notebook and
you can, you know,
train your own OCR for Angel Greek.
It works really well and
beats Google cloud vision with,
with the notebook.
So yeah, that's my bottom line on
OCR is if you have to do standard
stuff, you're very fortunate that
you're doing it today because GPT
has made things so much better.
Just really in the past like
six months has gone really good.
But that's like typed English or
maybe neat handwriting, you know.
But if you're doing yeah,
stuff that's more often being path,
this will be useful.
Okay, I have just a very quick word
about regression.
So again, in machine learning
the term regression refers
to the prediction of continuous
numbers, continuous outcomes.
And it basically works just like
classification.
You add a layer to your
neural network, but
now that layer is predicting
a continuous number instead of
predicting the class scores.
And one example of this that comes
up in economics a lot
is document image analysis
where we have some documents and
we want to get structured output.
You know, traditionally there were
no good ways to do this.
You'd have to bring together,
you know, lots of different tools
from different sources and
be pretty technically advanced.
So back, you know,
like five years ago now,
I worked with a couple of predogs
and Jake Carlson to design an open
source package called Layout Parser
for document image analysis.
And it tries to make it really
useful, friendly, you know,
this is an example from the paper.
Obviously it's an easy example but
it's, you know,
with a single line of code it's
detecting the layouts on this page.
This is an example of something
we did, you know,
that's a bit more complicated.
We want to customize it to detect
headlines, captions, et cetera,
newspapers.
If you send this
to like Google Cloud version,
this is what it does.
It reads it like
a single column book.
It's a problem with like
the OCR output too.
On sites like newspaper.com,
it gets scrambled up because
oftentimes because the layouts
weren't properly detected.
But with our
link transformer package we can
pretty easily detect layouts.
I will say that the thing about
layout detection is like you're
just, there's no, like, there's no
foundation model for doing this.
Like you're just starting with like
something trained on imagenet,
which is like Images of dogs and
cats and things like that.
And so you pretty much always need
to tune your own model if GPT
can't figure out your layouts,
which oftentimes it doesn't and
you need to figure them out.
We have base models on layout
parser, but you do oftentimes need
to train your own data.
But you can do that often with
hundreds of labels.
It's not super
costly in terms of labeling data.
This is another example.
This is the Japanese firm
data that I was talking about,
used to look at antitrust policies
that we divided into columns.
We use deep learning to recognize
the different pieces
of information.
All right, so that was a very
quick overview of regression.
Basically, if you
understand classification,
you understand regression.
And so in short, deep learning
provides really powerful tools for
processing unstructured data.
I found it very, very time
intensive to learn all this stuff
because there was no like resource.
I was very grateful.
Like you know, one of the first
classes on neural networks on kind
of even pre transformer was like at
Stanford in 2016.
Those are,
those lectures are still online.
I learned a lot from that.
But basically I had to go to
the Internet and learn a lot of
stuff myself, read papers.
And so I put this all into
a knowledge base,
linked a lot of resources.
I hope that makes it easier for
people to get familiar with
these tools.
Of course you might say,
well, these models aren't perfect.
Like how do we need to account for
that in research?
Which is what we
will talk about after lunch.
Sam.
