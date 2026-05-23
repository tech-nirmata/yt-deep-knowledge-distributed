---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 10d7f264-4228-48bb-a9a8-6cf163aa80d3
source_title: "Ep75 The Misleading Truth Behind IRR"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:38:48 UTC
extractor: nlm_bulk_extract.py
---

# Ep75 The Misleading Truth Behind IRR

## NotebookLM-extracted transcript (Google's ASR + indexing)

(music playing)
[JULES VAN BINSBERGEN] Welcome to the Lauder Institute
at the
University of Pennsylvania.
I'm Jules van Binsbergen,
director of the institute
and a finance professor at the
Wharton School.
[JONATHAN BERK] And I'm Jonathan Berk, a finance
professor at the
Graduate School of Business at
Stanford University.
This is the All Else Equal
podcast.
Welcome back, everybody.
Today, we're going to do an
episode on a topic that
Jules and I have spoken about
repeatedly for, I would say, as
long as we've known each other,
which is the internal rate of
return, and specifically using
the internal rate of return
as a criteria for making an investment decision.
[JULES VAN BINSBERGEN] Yeah, and Jonathan, I think that the use of
the IRR is ubiquitous, both in
the private sector
as well as in academia.
I mean, the number of finance
professors today that
essentially teach the IRR as a
complementary decision-making
criteria with the footnote that
it may have certain problems,
but still putting it almost on
equal footing with the net
present value or NPV criterion
is quite shocking to me.
[JONATHAN BERK] Yeah. So Jules, I teach the
introductory finance class.
It's a 10-week class.
I spend one week
on IRR
and why it is a horrendously bad investment rule.
And we wanted to talk about
this.
You and I now have a paper
which we're almost done
on the IRR rule.
And the paper makes
a strong claim, which
is that it's not exceptionally
bad in a few cases,
but it's always a bad
decision rule,
and that's a very strong claim,
and maybe we can explain
this on the show.
So why don't we start, Jules,
with explaining what is
the problem with the internal rate of return?
[JULES VAN BINSBERGEN] Well, before we do that, let's take even one
further step back, which is
let's talk about the
net present value and the IRR in
terms of how they're defined.
So generally, what we say is,
if you want to make a good
decision,
then you need to trade off costs
against benefits.
And so if you take the net of
those two things, you get the
net benefits of a decision.
But of course, when you make
a decision, generally the costs
that you have are not arriving
at the same
time as the benefits.
And so the field of finance is
particularly equipped to address
the issue of how do I trade off
costs and benefits that
don't happen at the same time?
And the object that we use to
trade those two things off is
what's called the discount rate.
And generally, we say that if
benefits happen further into
the future and/or are riskier,
that means that you value them
less as the risk goes up
and as the time that you have
to wait for them goes up.
[JONATHAN BERK] And what we do in
that case is when we bring all the cash flows to the present,
all the benefits to the present,
all the costs to the present,
and we subtract, and what you
called the benefits
outweigh the costs.
The word in finance is the net
present value of the
investment is positive.
So that just basically says all
the present value in
today's terms of all the
benefits exceed the present
value of all the costs.
And if that's positive, you make the investment decision.
[JULES VAN BINSBERGEN] Indeed.
And so when we use the acronym NPV, it has the N for net,
which means the net of costs and
benefits, and then PV,
present value, meaning that
everything has to be comparable
by bringing them all to today's
equivalent in terms of value,
and we use the discount rate to
do that.
Let's think about the intuition
of what a discount rate does.
So the way I always explain it in class is,
the discount rate essentially tells you
how important the present is
relative to the future.
So if the discount rate is
really low,
that means that the future is
very important to
you relative to the present.
If the discount rate is really
high, that means that
the future is not that important
to you in your decision-making.
Now, the internal rate of
return, or IRR, is already,
if you think about it, an interesting object in
and of itself in that it is a thought experiment.
It is a thought experiment that says, you know, we have
used the discount rate of, say,
for example, twelve percent.
But we're not going to be using
that twelve percent number.
We're going to do the thought
experiment where we ask what
should the discount rate
have been for the net
present value to be zero?
So nobody is arguing that that
is the correct discount rate.
No, we're doing a thought
experiment where we're
saying how far could we
push the discount rate in
many cases up if the net
present value was positive,
so that then we can see
how far we can push that
discount rate to push the net
present value to zero.
So in the usual investment rule, it's that the costs
come up front and the benefits come later.
So that means that if for the
normal,
the discount rate that we're
using,
the NPV is positive, if I now
start to push
the discount rate up, I make the
future,
which has the good stuff
happening,
less and less important, which
of course means that
the NPV will come down.
If I make the discount rate high
enough, I make the benefits so
irrelevant that eventually we
will reach the break-even point
where the NPV is exactly zero.
And that's how the internal rate
of return is defined.
And some people take the outcome
of that thought experiment
itself as a decision rule.
[JONATHAN BERK] So Jules, there's a very good
way to use the rate that comes
out of that thought experiment.
Because you, in many, many
cases, you don't know the
discount rate very accurately,
and what the thought
experiment tells you is
how far off can you be
such that your NPV's zero?
And so you can think of it as a break-even rate.
Yeah, and that's a very useful thing to know.
Because if you have a positive
NPV project and it turns out if
you're off by ten basis points
in your discount rate, it's a
zero NPV project, that tells you
you better
have a lot of confidence in your
discount rate.
But if, let's say, it's you need
to be off by five
percent in your discount rate,
most likely you'll know your f-
discount rate within five
percent, and so it's a
much more confident. And that's a very useful measure.
[JULES VAN BINSBERGEN] And so I agree that break-even quantities in general, when
we do sensitivity analysis, when
we make a decision,
I think is a useful thing to do.
We often think about the
break-even price or the
break-even quantity that we need
to sell or the break-even
tax rate, and in that sense, we
can also think about the
break-even discount rate.
And actually, Jonathan, I'm
happy that you bring
this up 'cause I think that is
the perfect terminology for it.
I don't think it should be
called the
internal rate of return.
There's nothing internal or rate
of return about
it, in my opinion.
It's just the break-even
discount rate.
That's a much better name for
it.
[JONATHAN BERK] Exactly.
The IRR investment rule works like this: invest whenever
the internal rate of return
exceeds the discount rate.
That's the rule.
Now, the problem begins when we
use it in another sense.
We say, well, if the discount
rate is less than the break-even
rate,
that must be a good deal.
And so we use that as a rule to
make an investment.
[JULES VAN BINSBERGEN] So now, Jonathan, we are not the
first
ones to bring up that this thing
may have problems,
and other people have pointed
out that in certain cases,
the usage of this internal rate
of return can have problems.
And so let's list them very clearly.
So the first one is
because we're asking for a rate that
makes the net present value
zero.
If the cash flows,
the net benefits that we are
using don't have a nice
pattern and they switch signs,
that means that this
thought experiment can
have multiple answers.
So it's possible that you get a
break-even discount
rate where the NPV is zero at
14%,
at 27%, and at 63%.
[JONATHAN BERK] And the intuition starts with the fact that the rule could
be exactly wrong in all cases.
So let's understand that.
So most people think of an
investment opportunity where
you, the costs are up front
and the benefits are later on.
[JULES VAN BINSBERGEN] Yes.
[JONATHAN BERK] But imagine an investment
opportunity where the
costs are later on and
the benefits are up front.
When I teach the class,
I teach a very salient
example, which is if
you're a textbook author,
often the way that works is
they pay you an upfront advance,
And then you have to incur the cost of writing the book.
In that case, the internal rate of return
investment rule gives you exactly the wrong answer,
and the reason is you're
essentially getting a loan.
So if you're doing a regular
investment,
and I tell you the internal rate
of return,
that is, the break-even discount
rate exceeds
the actual discount rate.
And then you say, "Okay, that's
a great deal for me,"
so I should take it."
But if you get a loan and I tell you the rate of the
loan exceeds the discount rate, you're going, "No, no,"
I don't want to pay that high
interest."
And so you could think of the
royalty example
as really a loan because you get
the money up front,
and then you have to make the
payments later,
which is the way a loan works.
Well, the way you get multiple
IRRs is after
the end of the work on the
textbook and you've paid the
advance back, you eventually
start getting royalties,
and so it becomes a mixture of a
loan and an investment.
And because of those mixtures,
the shape of the NPV curve
can be U-shaped, so you can get multiple IRRs.
[JULES VAN BINSBERGEN] So related to the example I gave earlier, Jonathan,
about the discount rate telling
you how important the future is,
now the good stuff that you're
talking about comes first
and the bad stuff comes later.
So obviously, if you now
increase
the discount rate, you make the
bad stuff
less important rather than the
good stuff.
And so therefore, the whole
intuition
switches around.
And so indeed, you have that
issue that now the IRR rule gets
it
completely wrong and you have to
really be careful.
But once you start to indeed mix scenarios and
some of the benefits happen in the future, and some of them happen now,
and some of the costs happen in
the future, once you start
to play with the discount rate,
what are you making more
important relative to the other
piece can totally depend.
And it's not even that you can
just get a U-shaped
curve for the IRR.
If there are multiple good and
bad things happening in
the future and they alternate,
you can really get tons of
different solutions for the IRR.
And now the question is, what am
I supposed to do with that?
You know, if I get six
different answers, what should
the rule now be?
[JONATHAN BERK] You know, Jules, this is well and good,
but many students, when I teach this, go, "Oh, he's being technical."
We can reverse the rule when,
uh, when needed,
when the cash flows come first."
[JULES VAN BINSBERGEN] Yes. (coughs)
[JONATHAN BERK] And there may be some truth to
that. I always
respond when they say that,
"Well, you know,
having a simple rule that is
invest whenever the p-NPV
is positive is a lot easier than
a rule that says invest
whenever the IRR exceeds the
discount rate,
except for and then a whole
bunch of exceptions."
But let's say you could do that.
That I don't think is the...
There's still
other issues with the IRR rule.
[JULES VAN BINSBERGEN] Yeah. So first, Jonathan, it's even possible that you
don't get a solution at all.
What if there is no break-even
point?
What are you supposed to do
then?
When your students ask the
question,
"Oh, you're being technical, I
can just change the rule,"
tell me, how are you gonna
change the rule
now if there isn't a solution?
Yeah. Right?
I always say to my students, if
I would raise my children
with a set of rules, and in
every situation
that they confront me with, I
have to change the rule
to make it work for that particular situation,
that's called not a rule.
Right?
[JONATHAN BERK] Exactly.
[JULES VAN BINSBERGEN] So the idea of rules should be that I can consistently
apply them and that they work
under all circumstances.
Otherwise, what are we really
doing?
But now let's go to what is an
even bigger
problem with the IRR.
[JONATHAN BERK] Well, one of the biggest
problems with the IRR is
what I would call scale, which
is very closely related
to another problem, which is the
timing of the cash flows.
But let's just talk about scale
because it's easy to understand.
As I tell my students, what would you rather have?
A 100% return on $1 or a 10% return on a billion dollars?
And it's pretty obvious.
You'd much rather have a 10%
return on a billion dollars.
But the IRR rule, since it's in
returns,
it's tempted to say, "I'd rather
have a 1,000% return
than a 10% return."
It ignores scale.
[JULES VAN BINSBERGEN] Yeah, for sure.
And so, of course, the implicit
assumption that people make when
they use the IRR is that you can somehow
make the scale irrelevant.
People say things like, "Well,
if you can get that super
high return that you just
mentioned on the one dollar,
why couldn't you just get it on
the billion dollars too?""
[JONATHAN BERK] And that, I think, is one of the
most fundamental mistakes
certainly academics make.
Probably business people don't
make that mistake,
because probably business people
fully understand the
decreasing returns to scale in
every single business.
In other words, it's suboptimal
to operate in the increasing returns
to scale part of the production function.
If you've got increasing returns to scale, increase
the size of the business.
And so any competent business is
going to be operating in
the decreasing returns to scale
part of the production function,
which means scale matters, and
which means you cannot
use a rule that ignores scale.
And it's very closely related to
the timing of the cash flows.
Because if you remember, the
rule is usually stated
on a per annum basis.
So if I tell you, you make a $1,000 investment today
and you will get back, say,
$200,000 in a year from now
or $200,000 in five years
from now,
the internal rate of return is
going to be different because
it's stated on an annual basis.
And then you'll say to me,
"Well, of course it's different,
you're getting the
cash flows later."
Yes, that's true.
But let's say you were getting
the cash flows
later, but the cash flows were
growing at a rate.
It's not been clear the IRR rule
gets it right,
because it depends very much on the rate at which
those cash flows are growing.
[JULES VAN BINSBERGEN] Absolutely.
And so Jonathan, now is a good
time, I think, to talk about
the paper that we have, right?
Because a lot of people say the
problems that you have pointed
out, they can occur, but there
are also many situations where
they don't have to occur.
And aren't we just fine, and
shouldn't we just try to
avoid those annoying scenarios
where the problems occur and
just stick with the good parts
of it, which is, let's just
hope and cross our fingers that
we're not in that part.
And so the paper that we wrote, I think makes a very strong
point, which says that
as soon as you can change the timing
of the cash flows through
payment plans,
so as soon as you allow for
financing of your investment,
meaning, for example, that you
don't have to make the full
investment in a machine or in a
plant or in a car today,
but you're allowed to pay it off
with a payment plan over time,
which of course is the same
thing as essentially taking
a loan for the investment that
you're making.
There exists a payment plan for every single positive
NPV investment where you can make these problems occur,
meaning that the scale can be
made such a problem that
essentially, if you can choose
the payment plan,
you can make the IRR any number
that you like higher
than the original IRR that you
got when you financed
the whole thing up front.
You can come up with scenarios
where you
get multiple solutions.
You can have a payment plan for
which you have no solutions.
So for that reason, these
pathologies of the IRR,
they're not just incidences.
They're such structural problems that they're
ubiquitous all the time.
[JONATHAN BERK] Yeah. So let's just state what the result of the paper is,
which is, if you allow
financing, every single project
will have a problem with IRR.
If you allow any financing.
Before we explain that, let's
just start with the intuition.
And let's start with a very
simple question.
If, you know, maybe some of
our listeners have already
thought about this, some of our
very
intelligent listeners, and they would have said, "You know, Jonathan,
you're telling us IRR is a terrible rule, but essentially,
that's the rule investors use
every day in the markets."
And it's true.
When investing in do a market
investment,
they calculate the rate of
return on that investment,
which is essentially the IRR.
And you're saying, "Well,
Jonathan,
surely according to you, that
means I'm making
mistakes all the time."
And my students ask me that.
My very brightest students who
are on the ball,
this is what they say to me when
we start doing
capital markets in that course.
And the answer is very simple.
An investment opportunity in the
market is usually a very
simple opportunity, which is
there's limited liability,
so the first cash flow is
negative, you buy,
all future cash flows are
positive.
Yep. So that immediately means
there's only one IRR.
And the second crucial part of
the investment
is we always assume that an
investor is small.
And what that means is the investor does not affect the price,
and that's equivalent to you can invest at any scale.
So the scale problem goes away.
[JULES VAN BINSBERGEN] Yeah, let's say definitely
indeed.
We assume that the scale
problem isn't there, because
assuming that
the investor is small is the
same as saying
there is no scale problem.
Let's be precise, right?
[JONATHAN BERK] Exactly.
[JULES VAN BINSBERGEN] Yes.
[JONATHAN BERK] And so the first thing I point
out to my students is,
that's true for you and me.
It's not true for a mutual fund
manager.
[JULES VAN BINSBERGEN] Or for Elon Musk.
[JONATHAN BERK] And, you know, the work that
Jules and I
have done in mutual funds is precisely predicated on
people making the mistake that a
that a mutual fund manager makes
an investment and he
doesn't affect the price.
And then if you realize that
that's of course unrealistic,
then no, you cannot use the IRR
rule to
evaluate a mutual fund manager.
No.
But keeping on that intuition
that if you're
small and you don't affect the
price, notice something,
that we always think about it as an investment where
we ignore finance.
But if we did not do that, then the IRR is arbitrary.
Because by simply financing, by
buying on margin,
you can change the return of
your investment.
So there's no fixed return on
investment if you allow
people to buy stock on margin.
So there's another implicit
assumption,
which was always talking about the return with no financing.
And so now let's think about the idea of a project where
you allow arbitrary financing.
[JULES VAN BINSBERGEN] Now, so, Jonathan, one thing
that we need
to add to that, right, is that
there's even a
link between allowing for
financing and assuming that
the scale is so small that you
wouldn't affect the price.
Because if I can aggressively
use financing, I can increase
the scale that I have to an arbitrary number that I like.
[JONATHAN BERK] Exactly.
So really, the set of conditions where you can use the return
to evaluate an investment
opportunity is very, very small.
Like, for example, private
equity,
people love to use IRRs to
evaluate their performance.
It's just incorrect in that
context.
In that context, the scale is
very limited.
The timing is very specific.
And so using IRR in the private
equity context, I think,
is one of the big mistakes
less sophisticated investors do.
I think more sophisticated
investors understand.
And when they are given
historical IRRs,
They take those IRRs with a grain of salt.
[JULES VAN BINSBERGEN] And there's one more thing that we need to talk about, Jonathan,
that the paper shows, which is
that if you take financing,
you can boost your IRR.
But if you take financing at
unfavorable rates,
you may still boost your IRR and
yet undermine your NPV,
meaning you are really hurting
the total value
that you're extracting, but
you're making your
IRR numbers look good.
So a really prevalent example of
this, particularly in the
sector that you just described, is if you know
that somebody uses IRR and you ask them, you know,
"Would you rather pay for the investment upfront or would you"
rather take a leasing plan at
an unfavorable interest rate?
If the person uses the IRR,
they will pick the leasing
plan at the unfavorable interest
rate and destroy value just
to make the IRR look better.
[JONATHAN BERK] Yes, and Jules,
I think we should talk
about the example you came
up with that I use every year
after you came up with it.
It's such a beautiful example.
You came up with an example
where you said, "Okay, let's
just consider an investment,
positive NPV investment,
standard, positive NPV."
The person makes an investment, and it pays off in a year, say.
And then what you do in that example is introduce a
financing plan where instead
of making the investment today,
you only invest one penny today.
And then you pay it back in the
future when your revenues come.
And obviously, that IRR is close
to infinity because you're
investing a
penny and you're getting
something in the future,
and you can invest half a penny
and a fraction of a penny,
and each time you reduce the
investment and move
the money to the future, you
send the IRR to infinity.
So the first part of the example you came up with is to show
students they can pick any IRR they want just based on
how much they want to invest
today using the financing plan.
And then the second part of
the example you came up with,
which I think is beautiful,
is you then consider a
financing plan at too high
a rate such that what happens
is the person borrows almost
all the required investment,
leaving just an epsilon amount
that they have to invest,
And then they, in the future, the payout has to be a
lot higher than epsilon.
[JULES VAN BINSBERGEN] Exactly.
But if epsilon is small, then the ratio of the
payout to the investment is
still a very high number.
In other words, you can send the
IRR to infinity, but if the
financing
rate is sufficiently above
market, you can
send the NPV towards zero.
So by taking an unattractive
financing plan, you can
generate a project for which the NPV approaches zero while
the IRR approaches infinity.
[JONATHAN BERK] And all the money goes to the person financing the project.
It's a wonderful example, very
simple example of a-
If you use the IRR rule, the
financing person can
take the NPV away from you.
[JULES VAN BINSBERGEN] Yeah, and I think that that is a
very important theme in
finance in general, Jonathan.
But today in class we had a long
discussion about this too,
where people were telling me
like, "Well, if everybody
uses EBITDA multiples, why
shouldn't we be using it?"
And I said to them, "Just like
with the IRR,
if I know you're using the wrong
decision-making
criterion, I can manipulate you.
Because if I know what the right
decision-making criterion is,
and I know you used the wrong one no matter what, then, you know,
I can take advantage of you.
[JONATHAN BERK] It's a very good point, Jules.
Excellent point.
And that's something that's so
important.
And you know, I just feel as if,
as finance professors,
we don't emphasize that enough.
When I talk about the NPV rule,
at one point early in
my career, I taught a class to
undergraduates,
and it was great.
And then one of the
undergraduates,
one of our best students, came
to see me afterwards,
and then he was telling me that
he was taking an accounting
class.
In the accounting class, they
were using the IRR rule,
and he said to the professor,
"No, no, no, no, no,"
"Professor Berk said, 'Got to use NPV.'"
And the professor started arguing with him.
And he said to me, "I couldn't argue back."
Professor Berk, why do you use
the NPV rule?"
And I was devastated because it
was quite clear I
hadn't taught anything.
And from that day onwards, I
said I would make sure
that my students understood.
And when I sit there and teach
NPV, I say to them,
"The NPV rule answers the only
question you're interested
in having answered, which is,
how much money can I make
on the investment opportunity?"
Any other rule, if it answers
that question, it has to be the
NPV
rule because the NPV rule
answers that question.
And if it doesn't answer that
question,
then it's not telling you how
much money you can make
on the investment opportunity.
He is telling you something
else.
[JULES VAN BINSBERGEN] Yeah.
[JONATHAN BERK] For sure. And as we play, since
it's telling
you something else, somebody can manipulate you.
[JULES VAN BINSBERGEN] Yeah. I love that example.
I mean, although I would say how much value do you add?
And that, of course, is the same
as the amount of
money that you make, agreed.
And indeed, in the end, a good
decision can only
be based on the correct
decision-making criterion.
So if I have three
decision-making criteria
and they give me three different
answers,
what am I supposed to do with
that?
[JONATHAN BERK] Well, they can't.
As you point out, there's always
a best
way of doing something.
[JULES VAN BINSBERGEN] Yes.
[JONATHAN BERK] So you can't have three
best ways of doing something.
And as it turns out, if your
objective is
to make as much money as
possible or to add as
much value as possible, that's
the NPV.
Those are synonymous.
So any other decision rule is not optimal.
It's not giving you what you want.
[JULES VAN BINSBERGEN] And so this most surprising answer to me that I get from
people is, \"Yeah, but
doesn't the IRR give
the same answer as the
NPV rule in many cases?
So is it then fine?\"
And then I'm like, \"Well, but
if it's giving the same answer,
then what do you need
the new decision-making
criterion for?
Didn't you already have the
decision-making criterion
then?\"
[JONATHAN BERK] But it isn't.
It does not give the
same answer as the NPV.
We just gave examples
where it doesn't,
and that can be used
to manipulate the situation.
Thanks for listening to All Else Equal podcast.
Please leave us a review at
Apple Podcasts.
We'd love to hear from our
listeners.
And be sure to catch our next
episode by subscribing
or following the show wherever
you listen to your podcasts.
For more information and
episodes, visit
allelseequalpodcast.com or follow us on LinkedIn.
The All Else Equal podcast is a joint production of
the Lauder Institute at the
University of Pennsylvania and
the Graduate School of Business
at Stanford University, and is
produced by University FM.
