---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 01b61b04-0ce2-42bc-94d4-f7388096bed8
source_title: "What Actually Makes AI Work: The Hidden Role of Materials | Catherine Li, MBA ’26"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:54:36 UTC
extractor: nlm_bulk_extract.py
---

# What Actually Makes AI Work: The Hidden Role of Materials | Catherine Li, MBA ’26

## NotebookLM-extracted transcript (Google's ASR + indexing)

(music playing)
[SPEAKER 1] I used to build light that you
couldn't see.
Near-infrared organic LEDs with
the emission wavelength
beyond 900 nanometers.
The kind of glow that doesn't
register to your eyes until
a sensor catches it.
I love that kind of idea.
The most powerful things are invisible.
For four years at Cornell, I was one of the few material
science engineering students in
my class.
At night, I spent time building
the hardware
that enables magic to happen.
The emitters that allow your
phone to recognize your face
in pitch darkness, the sensors
that allow autonomous vehicles
to see through a blinding fog.
And that lab taught me something
real quick.
Magic is easy to imagine,
yet materials are hard to manage.
On paper, our chemistry was
perfect,
but in the lab, the
reality was a constant battle
with operational lifetime.
With one unstable interface, you
suddenly have exciton
quenching, ion migrating, and
performance collapsing.
I learned that the material is
only as strong
as its weakest interface.
Now that's the bottleneck I think AI is running into today.
The future doesn't fail because
the idea isn't beautiful.
The future fails because
materials won't cooperate.
Hey, if you're interested in the
future of AI,
who here around isn't?
Please keep in mind that the
future of AI isn't governed
by model capabilities alone.
It's governed by three physical limits:
compute, data, and energy.
And today, I'm telling you that
underneath each of that
is a materials challenge.
The first limit is compute
efficiency.
Inside every AI chip, logic and
memory still sits
in different physical domains,
so data needs to be shuttling
back and forth all the time.
The processors can think incredibly fast,
but it generates enormous amounts of energy
moving bits across the interconnects,
and that energy becomes heat.
Push the system hard enough,
and it throttles.
Not because it can't compute,
but because
it can't dissipate heat.
Now, this is not a
latency problem,
it's a joules per bit problem.
High-bandwidth memory is the
industry's most important
response.
By leveraging 3D stacking and TSVs,
HBM puts compute adjacent to memory, collapsing the distance,
widening the interface, and
significantly improved
the energy efficiency.
But 3D stacking didn't remove
the problem, it moved it.
On scale up,
HBM can't grow indefinitely.
Thermal density, yield loss,
power delivery caps HBM scaling,
and that capacity lags model
growth.
On scale out,
Once the memory leaves the package and has to
travel across NVLink, across
the racks and data centers,
distance comes back.
Energy per bit goes up again.
You can't code your way
out of this problem.
This is not a software issue.
It's a materials integration
limit.
Until the day we have logic
and memory truly co-locate,
Energy compute efficiency
will always be the first wall that AI keeps running into.
The second limit is data
integrity.
If compute is how AI thinks,
data is how AI senses the world.
In the physical world, data is
never abstract.
Data is a measurement, and every
single measurement
passes through materials.
To understand the real world, we
need stable,
high-fidelity signals across multiple modalities.
Vision, touch, force, depth, motion.
Each is bounded
by sensor physics.
Take vision, for example.
Cameras are still suffering
from low light, glare,
and thermal noises.
You can't infer details that
never get to the camera.
Missing photons aren't
a mo- model problem.
Then there's the
stability challenge.
Materials take on
moisture, optics shift,
electronic drift with heat loss and time.
So the real-world input
slowly changes into something
different.
You can train a robot to hold an
egg in the lap perfectly,
but six months later in the real
kitchen,
the sensors have changed.
The signal that used to mean
gentle means crush.
This is not the robot being
confused.
It's the nervous system line.
And once you have that, your data isn't just noisy,
it's systematically wrong.
That's why physical AI feels
brittle outside of the lab,
not because the intelligence
isn't there,
but because the interface to
reality is unstable,
and what it looks like to be a
data problem is underneath
a material stability challenge.
The third limit is energy waste.
Energy is the invisible tax that everybody pays.
Every wire, every contact, every interface
wastes energy in the form of
heat.
In 2024,
data center consumes roughly 415
terawatt-hours,
roughly eight times of the New
York City electricity
consumption annually.
And in the base case, IEA
projects that number to
be double by 2030.
And most of that energy isn't
used for compute.
It's used for moving signals and removing heat.
So we get creative.
We start to talk about AI factories next
to nuclear plants.
We talk about small modular
reactors, solar breakthroughs,
geothermal, and even data
centers in the space.
And every single one of those
solutions runs
straight back into materials.
Energy isn't a motor problem.
It's a material science
limitation problem.
As long as we keep wasting energy in the form of heat,
and as long as interconnects and power delivery keep setting
the ceiling for performance,
intelligence remains heavy,
expensive, and centralized,
And that's the third limit that
AI will keep running into.
When I was in the lab, our
device worked beautifully
Until they meet the real world.
Moisture slips through its-
Moisture slips through the
seals,
temperature swings pulled layers
apart, contact corroded.
And that was the first real
lesson I learned.
To put intelligence into the
world,
you need to first package it
against the world.
Materials have edge cases, and
edge cases are
where products die.
So that's what we do.
As material scientists,
we fight the slow battles with heat loss and time,
and once those limits move, the
whole industry reorganizes.
Here we are done.
The next breakthrough of AI
wouldn't come from
mo- smarter models alone.
It will be coming from materials
that enable
compute, data, energy efficient
enough to scale.
And in the short term, the
progress will be
unglamorous, but it will be critical.
Better packaging, better interface,
better thermal pathways, more
stable substrate.
In AI scale, every few
percentage points
of performance improving
sets the difference between the
demo and the deployment.
In the long run, the
breakthrough
won't come on schedule.
It will be at constraints where
we've been grinding for years:
superconductors that actually
works, quantum computing
that are coherent enough to be stable,
and materials that improve efficiency and lower loss and
enable intelligence information
to behave differently
than what they do today.
I started with the invisible
light that you can't see.
A glow that's beyond 900
nanometers only
a sensor could catch.
And that invisible technology
ended up inside
billions of devices today.
And the next era will
be built the same way.
Quietly, physically,
and then all at once.
So if you're chasing your AI
dream or if you're investing
in this space, please keep in
mind that the future of AI
isn't about what it can think.
It's about whether it
can survive the contact
with the physical world.
And that future won't
be defined by models.
It will be defined by materials.
Thank you.
(applause and cheering,
music playing)
