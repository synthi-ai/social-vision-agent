---
name: thread-writer
description: Write compelling multi-post threads for X/Twitter that build narrative momentum and drive follows. Activate for thread-format content.
license: MIT
metadata:
  agents: "writer"
  category: content
---

# Thread Writer Skill

## 1. Overview

The Thread Writer skill transforms a single topic into a multi-tweet narrative that holds
attention across 4-15 tweets. Threads are the highest-value content format on X/Twitter
because they combine the virality of a single tweet with the depth of a blog post.

A well-crafted thread achieves three things simultaneously:
- The **opener** goes viral on its own in the timeline
- The **body** delivers genuine value that earns follows
- The **closer** converts readers into community members

This skill activates whenever the content pipeline requires thread-format output, whether
from `weekly_brief.yaml` campaigns marked as `format: thread` or when the strategist node
determines that a topic has enough depth to warrant a multi-tweet treatment.

## 2. Core Capabilities

- Architect thread structures from 4 to 15 tweets with narrative coherence
- Write openers that function as standalone viral tweets AND thread launchers
- Optimize each individual tweet for character count (200-260 sweet spot)
- Apply the standalone+connected principle: every tweet works alone, flows in sequence
- Place visual tweets (images, code screenshots, charts) at strategic positions
- Craft closers that convert readers into followers and drive profile visits
- Adapt thread style by content type (tutorial, opinion, case study, resource list)
- Generate numbered vs. flowing thread formats based on content structure
- Create engagement hooks at intervals to prevent mid-thread drop-off
- Design self-referencing CTAs that chain threads into a content flywheel
- Plan thread scheduling strategy for maximum reach and engagement

## 3. When to Use This Skill

Activate the thread-writer skill when ANY of these conditions are true:

| Trigger Condition | Example |
|---|---|
| `weekly_brief.yaml` specifies `format: thread` | `format: thread` in campaign config |
| Topic has 3+ distinct sub-points | "5 lessons from scaling our AI pipeline" |
| Content requires step-by-step explanation | Tutorial, how-to, setup guide |
| A resource list has 4+ items | Tool recommendations, reading lists |
| Case study with before/after narrative | "How we reduced latency from 2s to 50ms" |
| Strategist node flags topic as thread-worthy | Depth score >= 7/10 in strategy output |
| Content repurposing from long-form source | Blog post, talk transcript, documentation |

Do NOT use thread format when:
- The idea fits in a single tweet (under 280 characters with impact)
- The topic is time-sensitive breaking news (single tweet + quote-tweets instead)
- The audience data shows thread fatigue (3+ threads in last 48 hours)

## 4. Detailed Workflow

### Step 1: Topic Decomposition

Break the input topic into atomic units. Each unit must pass the "one breath" test:
can you explain it in a single breath to someone at a coffee shop?

```
Input: "How we built our AI agent system with LangGraph"
Atomic units:
  1. The problem we were solving (why agents?)
  2. Why we chose LangGraph over alternatives
  3. Our graph architecture (8 nodes)
  4. The hardest node to build (human-in-the-loop)
  5. Error recovery patterns that saved us
  6. Performance numbers (before/after)
  7. What we'd do differently
```

### Step 2: Determine Thread Length

Use this decision matrix:

| Content Type | Optimal Tweets | Rationale |
|---|---|---|
| Tutorial / How-to | 7-10 | Each step = 1 tweet, plus opener and closer |
| Opinion / Hot take | 4-6 | Beyond 6, opinion threads lose sharpness |
| Case study | 5-8 | Setup, challenge, approach, results, lessons |
| Tool / Resource list | 8-12 | 1 tool per tweet with brief context |
| Story / Narrative | 6-9 | Classic story arc needs room but not sprawl |
| Comparison / Versus | 5-7 | Setup, side A, side B, nuance, verdict |
| Data breakdown | 6-10 | One data point or chart per tweet |

### Step 3: Write the Opener (Tweet 1)

The opener is the most critical tweet. It appears alone in the timeline and must do two jobs:
1. **Stop the scroll** as a standalone tweet
2. **Promise enough value** to justify clicking "Show this thread"

#### Opener Formulas

**The Numbered Promise:**
```
I spent 6 months building AI agents with LangGraph.

Here are 7 hard-won lessons that will save you weeks of debugging.

A thread:
```

**The Contrarian Setup:**
```
Most AI agent tutorials teach you the wrong architecture.

After shipping 3 production systems, here's what actually works:
```

**The Proof-First:**
```
We went from 12-second response times to 340ms.

The secret wasn't a faster model.

Here's exactly what we did (and how you can too):
```

**The Story Hook:**
```
At 3 AM, our agent pipeline started hallucinating prices to customers.

What happened next completely changed how we build AI systems.
```

**The Curiosity Gap:**
```
There's a LangGraph pattern that 90% of tutorials skip.

It's the difference between a demo and a production system.

Let me show you:
```

Rules for openers:
- First line MUST be under 100 characters (visible before "see more" on mobile)
- Include a thread indicator: "A thread:", "Thread:", or the 1/n pattern
- Never start with "GM" or "Hey everyone" -- zero scroll-stopping power
- Avoid links in the opener (algorithm penalty on X)

### Step 4: Build the Body (Tweets 2 through N-1)

Each body tweet follows the ACE structure:
- **A**ssertion: State the point in one sentence
- **C**ompression: Add the evidence, example, or detail in 1-2 sentences
- **E**xit hook: End with something that pulls readers to the next tweet

#### Body Tweet Templates

**The Teaching Tweet:**
```
3/ Error recovery is where most agent graphs break.

Our pattern: wrap every node in a try/except that writes
a structured error to state, then routes to a recovery node.

The recovery node has 3 strategies: retry, skip, or escalate.

This alone eliminated 80% of our production failures.
```

**The Comparison Tweet:**
```
5/ We tested Ollama (Llama 4) vs. GPT-4o for our writer node.

Ollama: 2.1s avg, $0 cost, 7.2/10 quality
GPT-4o: 0.8s avg, $0.03/call, 8.1/10 quality

For social media content, the quality gap didn't justify 100x cost.
```

**The Visual Tweet (image placement):**
```
4/ Here's our actual graph architecture:

[IMAGE: LangGraph node diagram showing 8 nodes with edges]

researcher -> strategist -> product_expert -> writer ->
visual -> optimizer -> human_approval -> publisher

Each arrow is a conditional edge. The magic is in the conditions.
```

**The Micro-Story Tweet:**
```
6/ The moment everything clicked:

We added human_approval with interrupt_before, expecting friction.

Instead, our content team said: "This is the first AI tool
that actually asks for my opinion instead of replacing it."

That's when I realized we'd built the right thing.
```

#### Body Tweet Rules

1. **Character count**: Aim for 200-260 characters per tweet. Under 200 feels thin.
   Over 260 means you're cramming two ideas into one tweet.
2. **Transitions**: Use numbered format (2/, 3/, 4/) OR flowing transitions
   ("But here's the thing...", "The breakthrough came when..."). Never mix both.
3. **Image placement**: Place visuals at tweet 3 or 4 (peak attention), and again
   at tweet N-2 (re-engagement before closer). Never back-to-back image tweets.
4. **The "mini-hook" rule**: Every 3rd body tweet should end with a forward pull:
   "But the real surprise came next...", "This is good. The next one is better."
5. **Standalone test**: Cover the tweets before and after. Does this tweet still
   deliver value to someone who only sees it as a quote-tweet? If not, rewrite.
6. **No filler tweets**: If a tweet only says "Let me explain..." or "Here's the
   thing..." without delivering substance, delete it. Every tweet must earn its spot.

### Step 5: Craft the Closer (Final Tweet)

The closer converts thread readers into followers. It has three components:

**Component 1 -- Takeaway Summary (1 sentence):**
Distill the entire thread into one memorable line.

**Component 2 -- CTA (1-2 sentences):**
Give readers a specific action. Never generic "follow me."

**Component 3 -- Thread Chain (optional, 1 sentence):**
Link to your next thread or a related past thread.

#### Closer Templates

**The Recap + Follow CTA:**
```
10/ TL;DR: Production AI agents need error recovery at every node,
human-in-the-loop for trust, and cost optimization from day one.

I write threads like this every week about building AI systems
that actually ship.

Follow @handle so you don't miss the next one.
```

**The Resource + Save CTA:**
```
8/ To summarize:

- Use LangGraph for stateful workflows
- Ollama for cost-effective inference
- PostgreSQL for flexible post storage
- Human approval before publish

Bookmark this thread. You'll need it.

RT the first tweet to help other builders find it.
```

**The Teaser + Chain CTA:**
```
7/ Building the graph was the easy part.

The hard part? Getting the content quality right.

Next week I'll break down our prompt engineering patterns
for each of the 8 nodes.

Follow + turn on notifications to catch it.
```

### Step 6: Polish and Optimize

Run the full thread through these checks before output:

1. **Read aloud test**: Read the entire thread out loud. Flag any tweet that
   sounds unnatural or where you stumble.
2. **Character audit**: No tweet over 280 characters. Flag tweets under 140
   (probably too thin) or over 260 (probably trying to do too much).
3. **Drop-off audit**: Read only tweets 1, 4, and the last tweet. Does the
   thread still make sense? Those are the three tweets most people will see.
4. **Visual spacing**: Ensure no more than 3 consecutive text-only tweets.
   Insert an image, code block, or stat-heavy tweet to break monotony.
5. **Link placement**: Links belong ONLY in the final tweet or second-to-last
   tweet. Never in tweet 1 (algorithm penalty) or body tweets (breaks flow).

### Step 7: Schedule Strategy

| Timing Factor | Recommendation |
|---|---|
| Best days for threads | Tuesday, Wednesday, Thursday |
| Best posting time | 8-10 AM in target audience timezone |
| Reply window | Author must reply to comments within 2 hours of posting |
| Thread spacing | No more than 2 threads per week (avoids fatigue) |
| Follow-up tweet | 4-6 hours after posting, quote-tweet the opener with a new angle |

## 5. Frameworks and Models

### Thread Architecture Patterns

| Pattern | Structure | Best For |
|---|---|---|
| **Linear** | Point 1 -> Point 2 -> ... -> Point N | Tutorials, step-by-step |
| **Pyramid** | Big claim -> Supporting evidence -> Details | Opinion, analysis |
| **Inverted Pyramid** | Details -> Build up -> Big reveal | Stories, case studies |
| **Hub-and-Spoke** | Central theme -> Related angles | Resource lists, comparisons |
| **Problem-Solution** | Problem -> Failed approaches -> Solution | Product, how-to |
| **Chronological** | Then -> Then -> Then -> Now | Journey, growth stories |

### Narrative Arc Model

Every thread should follow a tension curve:

```
Engagement
    ^
    |     *  (tweet 3-4: peak curiosity / key insight)
    |    / \
    |   /   \   *  (tweet N-2: second peak / surprising detail)
    |  /     \ / \
    | /       *   \  * (closer: resolution + CTA)
    |*              \/
    +--1--2--3--4--5--6--7--8--> Tweet number
    (opener)
```

The "valley" between peaks (tweets 5-6 in an 8-tweet thread) is where most
readers drop off. Place your most surprising fact, your best image, or a
micro-cliffhanger there to maintain momentum.

### The SPACE Framework for Individual Tweets

| Letter | Principle | Example |
|---|---|---|
| **S** | Specific | "340ms response time" not "really fast" |
| **P** | Personal | "We learned" not "It is known that" |
| **A** | Actionable | Include a takeaway the reader can use today |
| **C** | Concise | One idea per tweet, no exceptions |
| **E** | Engaging | End with curiosity, not a period that invites scrolling past |

## 6. Platform-Specific Guidelines

### X / Twitter (Primary Platform for Threads)

**Character limits:**
- 280 characters per tweet for free accounts
- 4,000 characters per tweet for Premium subscribers (but avoid using full limit;
  long tweets break the thread rhythm)
- Optimal per-tweet length: 200-260 characters

**Threading mechanics:**
- Use the native thread feature (reply to your own tweet)
- Number format: "1/", "2/", etc. OR no numbers (flowing narrative)
- Never use "(thread)" or "(1/n)" in the opener -- it's redundant with the
  thread indicator icon

**Algorithm considerations:**
- Threads get 30-50% more impressions than single tweets on average
- The opener tweet receives 10x more impressions than later tweets
- Engagement on the opener (likes, RTs in first 30 minutes) determines
  how many people see the full thread
- Self-replies within 1 minute of posting perform better than delayed replies

**Media in threads:**
- Images: 1600x900 or 1200x675 (16:9 ratio)
- Max 4 images per tweet within a thread
- GIFs reduce impression reach vs. static images in thread context
- Code screenshots outperform plain text for technical content

### LinkedIn (Thread Adaptation: Carousel)

Threads on LinkedIn exist as carousel posts (PDF uploads) or long-form posts
with line breaks simulating a thread structure.

**Carousel adaptation:**
- Convert each tweet into one carousel slide
- Slide dimensions: 1080x1350 (4:5 portrait) for maximum feed real estate
- Slide 1 = thread opener (bold title + hook)
- Final slide = CTA + profile branding
- Limit: 10 slides per carousel for optimal completion rate
- Use consistent font, color scheme from visual-branding skill

**Long-form post adaptation:**
- Convert each tweet into a short paragraph (2-3 sentences)
- Separate paragraphs with blank lines
- Use "---" or whitespace to simulate tweet boundaries
- Add the key insight as a pull-quote with line breaks around it
- Max length: 3,000 characters (LinkedIn post limit)

### TikTok (Thread Adaptation: Multi-Part Series)

TikTok doesn't support text threads, so adapt to:
- **Video series**: "Part 1/7: How we built AI agents" in caption
- **Carousel posts**: Up to 35 slides per carousel on TikTok
- **Pin structure**: Pin Part 1 to profile; link others in comments

**Caption adaptation per part:**
- Keep under 150 characters for visibility
- Include part number prominently: "Part 3/7"
- End with "Follow for Part [N+1]" CTA
- Use 3-5 hashtags per part (see hashtag-strategy skill)

### Facebook (Thread Adaptation: Multi-Image Post or Series)

**Multi-image album:**
- Each tweet becomes an image card with text overlay
- Album title = thread opener
- Facebook auto-expands albums, giving each card visibility

**Post series:**
- Use Facebook's "Series" feature for connected posts
- One post per day across the week
- Cross-link in comments: "Missed Part 1? [link]"

## 7. Quality Checklist

Before submitting a thread for human_approval, verify:

- [ ] Opener works as a standalone viral tweet (cover the thread, would you RT this?)
- [ ] Every tweet passes the standalone+connected test
- [ ] No tweet exceeds 280 characters
- [ ] 80% of tweets fall in the 200-260 character sweet spot
- [ ] Thread has exactly one clear topic (no scope creep)
- [ ] At least one image/visual tweet in position 3 or 4
- [ ] No consecutive text-only tweets beyond 3 in a row
- [ ] Mini-hooks placed every 3rd tweet to prevent drop-off
- [ ] Closer includes a specific CTA (not generic "follow me")
- [ ] No links in tweets 1 through N-2 (only in final or second-to-last tweet)
- [ ] Thread length matches content type guidelines (see Step 2 table)
- [ ] Numbered format is consistent (all numbered or all flowing, never mixed)
- [ ] No "filler" tweets that don't deliver value
- [ ] Tone is conversational, not corporate or academic
- [ ] Thread has been read aloud without stumbling

## 8. Output Format Template

The writer node should output threads in the following JSON structure:

```json
{
  "thread_id": "uuid-v4",
  "platform": "x_twitter",
  "format": "thread",
  "topic": "How we built production AI agents with LangGraph",
  "thread_length": 8,
  "architecture_pattern": "problem-solution",
  "numbering_style": "numbered",
  "tweets": [
    {
      "position": 1,
      "role": "opener",
      "content": "We spent 6 months building AI agents that actually ship to production.\n\nNot demos. Not prototypes. Real systems handling real users.\n\nHere are 7 lessons that will save you months of pain.\n\nA thread:",
      "character_count": 218,
      "has_media": false,
      "media_url": null,
      "media_alt_text": null,
      "engagement_hook": "numbered_promise"
    },
    {
      "position": 2,
      "role": "body",
      "content": "2/ Lesson 1: Your graph architecture IS your product.\n\nWe tried a linear pipeline first. It broke immediately.\n\nThe fix: LangGraph with conditional edges.\n\nEach node does one thing. Each edge decides what happens next.\n\nSimple to debug. Easy to extend.",
      "character_count": 261,
      "has_media": false,
      "media_url": null,
      "media_alt_text": null,
      "engagement_hook": null
    },
    {
      "position": 8,
      "role": "closer",
      "content": "8/ TL;DR:\n\n- Graph architecture > linear pipeline\n- Error recovery in every node\n- Human-in-the-loop builds trust\n- Local models cut costs 100x\n\nI'm writing a deep-dive on our prompt engineering next week.\n\nFollow @handle and turn on notifications to catch it.",
      "character_count": 256,
      "has_media": false,
      "media_url": null,
      "media_alt_text": null,
      "engagement_hook": "teaser_chain"
    }
  ],
  "scheduling": {
    "recommended_day": "Tuesday",
    "recommended_time_utc": "14:00",
    "follow_up_quote_tweet_hours": 5
  },
  "metadata": {
    "estimated_read_time_seconds": 90,
    "target_audience": "AI engineers and developers",
    "content_pillar": "technical_credibility",
    "campaign_id": "weekly_brief_2026_w13"
  }
}
```

## 9. Complete Examples

### Example 1: Tutorial Thread (Before and After)

**BEFORE (weak thread):**
```
Tweet 1: "Let me tell you about LangGraph. It's really cool. Thread:"
Tweet 2: "LangGraph is a framework for building agents."
Tweet 3: "You can define nodes and edges."
Tweet 4: "It supports state management."
Tweet 5: "We use it at our company."
Tweet 6: "Follow me for more!"
```

Problems: Generic opener, no scroll-stopping hook, tweets are thin (under 100 chars),
no specifics, no images, filler content, weak CTA.

**AFTER (strong thread):**
```
Tweet 1: "We replaced 2,000 lines of spaghetti agent code with 200 lines of LangGraph.

Same functionality. 10x fewer bugs. 3x faster to add features.

Here's the exact architecture we used (and how to build it yourself):

Thread:"

Tweet 2: "2/ First, forget everything you know about agent 'frameworks.'

Most of them are wrappers around a while loop with an LLM call inside.

LangGraph is different: it's a state machine where each node is a function
and each edge is a routing decision.

That distinction matters."

Tweet 3: "3/ Here's our actual production graph:

[IMAGE: Clean diagram showing 8 nodes with labeled edges]

8 nodes. Clear responsibility boundaries.
The researcher never writes. The writer never researches.

Separation of concerns isn't just for backend code."

Tweet 4: "4/ The node that took us longest to get right: human_approval.

We use LangGraph's interrupt_before to pause the graph mid-execution.

A human reviews, edits, or rejects. Then the graph resumes.

It took 3 days to build. It saved us from publishing an AI hallucination
to 50K followers."

Tweet 5: "5/ Error recovery was our secret weapon.

Every node wraps its LLM call in a try/except that writes structured
errors to the graph state.

A recovery node inspects the error and decides: retry, skip, or escalate.

Production uptime went from 94% to 99.7%."

Tweet 6: "6/ Cost was the surprise.

We assumed GPT-4o was necessary. Tested Ollama with Llama 4 locally.

Content quality: 7.2/10 vs 8.1/10
Cost per post: $0.00 vs $0.03
Monthly savings: ~$900

For social media copy, local models win on ROI. It's not even close."

Tweet 7: "7/ What we'd do differently:

- Start with PostgreSQL from day 1 (SQLite didn't scale)
- Add human-in-the-loop earlier (trust is earned, not assumed)
- Write integration tests for the full graph, not just unit tests per node

These 3 mistakes cost us ~3 weeks."

Tweet 8: "8/ TL;DR: Production AI agents need:

- Graph architecture (not linear pipelines)
- Error recovery at every node
- Human-in-the-loop for trust
- Local models for cost sanity

I'm breaking down our prompt engineering for each node next week.

Follow @handle so you don't miss it.

RT tweet 1 to help other builders."
```

### Example 2: Opinion Thread (Before and After)

**BEFORE (weak thread):**
```
Tweet 1: "Hot take about AI"
Tweet 2: "AI is changing everything"
Tweet 3: "But people don't realize how"
Tweet 4: "Here's my opinion"
Tweet 5: "Follow for more AI content"
```

**AFTER (strong thread):**
```
Tweet 1: "Unpopular opinion: RAG is becoming a crutch.

90% of RAG implementations I've reviewed are solving a prompting problem
with an infrastructure problem.

Here's what I mean (and what to do instead):"

Tweet 2: "2/ The pattern I keep seeing:

'Our LLM doesn't know about our docs.'
'Solution: build a RAG pipeline.'

But the real question is: does the LLM need ALL your docs, or just
the right 3 paragraphs?

Most teams skip the curation step entirely."

Tweet 3: "3/ We tested this with a client last month.

Their RAG pipeline: 4 services, 2 vector DBs, 15s query time.

Our replacement: a curated prompt with 12 key paragraphs, updated weekly.

Accuracy went UP. Latency dropped to 800ms. Infra cost: $0.

[IMAGE: Side-by-side architecture diagrams]"

Tweet 4: "4/ I'm not saying RAG is useless. It's essential when:

- Your knowledge base changes hourly
- You have 100K+ documents
- Users ask unpredictable questions

But for 80% of enterprise use cases? A well-maintained system prompt
with curated context outperforms RAG.

Fight me."

Tweet 5: "5/ The deeper problem: RAG gives teams a false sense of completeness.

'We indexed all our docs, so the AI knows everything.'

No. Your AI knows everything badly. Retrieval quality is the bottleneck,
and most teams never measure it.

Precision matters more than recall."

Tweet 6: "6/ My recommendation:

Before building RAG, try this:
1. List the 20 questions users actually ask
2. Curate the best answer for each
3. Put those in your system prompt
4. Measure accuracy

If it's above 85%, you might not need RAG at all.

Save yourself 3 months of infra work."
```

## 10. Common Mistakes

| Mistake | Why It's Bad | Better Approach |
|---|---|---|
| Generic opener ("Let me tell you about...") | Zero scroll-stopping power; gets buried in timeline | Lead with a result, number, or contrarian claim |
| Every tweet under 140 characters | Feels lazy; Twitter shows longer tweets more prominently | Aim for 200-260 chars with substance in every tweet |
| Mixing numbered and flowing styles | Confuses readers about thread structure | Pick one style and commit for the entire thread |
| Putting links in tweet 1 | X algorithm suppresses tweets with links | Move all links to the final tweet |
| No images in the thread | Text-only threads have 40% lower engagement | Add at least 1 image at position 3 or 4 |
| Filler tweets ("Let me explain...") | Readers drop off at the first tweet that wastes their time | Every tweet must deliver a fact, insight, or story beat |
| Thread longer than 15 tweets | Completion rate drops below 20% beyond tweet 12 | Split into two threads; tease Part 2 in the closer |
| No CTA in the closer | Readers finish and scroll away without following | Always include a specific, value-aligned CTA |
| Posting threads on weekends | Thread engagement drops 35-45% on Saturday/Sunday | Schedule for Tuesday-Thursday, 8-10 AM target timezone |
| Not replying to comments | Thread algorithm boost depends on author engagement | Reply to every comment within the first 2 hours |
| Back-to-back image tweets | Breaks reading rhythm; feels like a slideshow | Space images at least 2 tweets apart |
| Thread about everything at once | Unclear value proposition; readers don't know what they'll learn | One topic per thread, stated clearly in the opener |

## 11. Advanced Techniques

### Quote-Tweet Thread Integration

After posting a thread, create a quote-tweet of your opener 4-6 hours later with a
"hot take" angle that attracts a different segment of your audience:

```
Original opener: "7 lessons from building AI agents with LangGraph"
Quote-tweet: "The most controversial lesson from this thread: local models beat
GPT-4o for social media content. Here's the data: [quote-tweet of opener]"
```

This gives the thread a second wave of visibility without reposting.

### Thread Chains (Content Flywheel)

Create a series of connected threads that reference each other:

```
Thread 1 closer: "Next week: how we engineered the prompts for each node."
Thread 2 opener: "Last week I shared our LangGraph architecture. This week: the prompts."
Thread 2 closer: "Next: how we handle error recovery in production."
Thread 3 opener: "Part 3 of our AI agents series..."
```

Each thread drives followers who want the next installment. Pin the "index" tweet
to your profile that lists all threads in the series.

### The "Jab-Jab-Hook" Thread Pattern

Not every thread should be a tutorial. Mix thread types across the week:

```
Monday:    Single opinion tweet (jab)
Tuesday:   Thread -- deep tutorial (hook)
Wednesday: Quote-tweet industry news (jab)
Thursday:  Thread -- case study (hook)
Friday:    Single behind-the-scenes tweet (jab)
```

This prevents thread fatigue while building anticipation for your long-form content.

### Engagement Farming Within Threads

At tweet 4 or 5, insert an engagement bait tweet that invites replies WITHOUT
breaking the narrative:

```
"5/ This is where it gets interesting.

Before I share the results, quick poll:

What do you think won? Ollama (local) or GPT-4o (cloud)?

Reply with your guess. I'll share the answer in the next tweet."
```

This creates a reply thread that boosts the overall thread's visibility.

### Thread Repurposing Pipeline

Every thread should be designed for repurposing from the start:

| Thread Component | Repurposed As |
|---|---|
| Opener | Standalone tweet (reshare in 2 weeks) |
| Image tweets | LinkedIn carousel slides |
| Full thread | Blog post draft (expand each tweet to a paragraph) |
| Key insight tweet | Instagram/TikTok text overlay |
| Stats tweet | Infographic for Pinterest/LinkedIn |

## 12. Settings and Configuration

### weekly_brief.yaml Thread Configuration

```yaml
campaigns:
  - name: "AI Agents Deep Dive"
    format: thread
    thread_config:
      length: 8
      numbering: true
      architecture: "problem-solution"
      images:
        - position: 3
          url: "https://cdn.example.com/graph-architecture.png"
          alt_text: "LangGraph node diagram with 8 connected nodes"
        - position: 6
          url: "https://cdn.example.com/cost-comparison.png"
          alt_text: "Bar chart comparing Ollama vs GPT-4o costs"
      cta_style: "teaser_chain"
      schedule:
        day: "tuesday"
        time_utc: "14:00"
```

### Writer Node Thread Parameters

The writer node in `src/graph/nodes.py` accepts these thread-specific parameters
via the graph state:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `thread_length` | int | 8 | Number of tweets in the thread |
| `numbering_style` | str | "numbered" | "numbered" or "flowing" |
| `architecture` | str | "linear" | Thread structure pattern |
| `image_positions` | list[int] | [3] | Tweet positions for images |
| `cta_style` | str | "follow" | "follow", "save", "teaser_chain", "resource" |
| `max_chars_per_tweet` | int | 280 | Character limit per tweet |
| `target_chars_per_tweet` | int | 240 | Target character count for optimal engagement |

### LLM Prompt Template for Thread Generation

The writer node should structure its prompt to the LLM as follows:

```
You are writing a {thread_length}-tweet thread about: {topic}

Thread architecture: {architecture}
Numbering: {numbering_style}

Requirements:
- Tweet 1 must work as a standalone viral tweet
- Each tweet: 200-260 characters
- Place images at positions: {image_positions}
- Closer CTA style: {cta_style}
- Every tweet must pass the standalone+connected test

Topic context from researcher:
{research_context}

Strategy from strategist:
{strategy_context}

Write the full thread now.
```

## 13. Notes

- Thread performance data should be stored in PostgreSQL (`posts` collection) with
  `format: "thread"` and individual tweet metrics for per-position analysis.
- The human_approval node should display threads with tweet numbers and character
  counts so the reviewer can quickly spot issues.
- When Groq is used as fallback instead of Ollama, thread quality tends to be
  slightly higher but the output format may need additional parsing.
- Thread performance varies significantly by niche. Tech/developer threads peak
  at 7-9 tweets, while marketing/business threads perform best at 5-7 tweets.
  Adjust the defaults in `weekly_brief.yaml` per campaign.
- The optimizer node should check thread-specific metrics: per-tweet character count,
  image placement, CTA presence in closer, and numbering consistency.
- Consider A/B testing: alternate between numbered and flowing thread styles across
  weeks and track which format drives more followers for your specific audience.
