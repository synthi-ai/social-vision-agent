---
name: trend-researcher
description: Research and analyze current industry trends, competitor activity,
  and viral content patterns to inform content strategy. Activate for
  research-driven content planning.
license: MIT
metadata:
  agents: "strategist,writer"
  category: research
---

# Trend Researcher Skill

## 1. Overview

The Trend Researcher skill provides a systematic methodology for identifying,
validating, and converting industry trends into high-performing social media content.
It replaces ad-hoc research with a structured 5-step framework that ensures every
content decision is backed by data, timing analysis, and strategic fit assessment.

This skill activates during the strategist and writer nodes of the content graph.
It sits at the beginning of the content pipeline, feeding validated trend intelligence
into downstream content creation, ensuring posts are timely, relevant, and differentiated
from competitor output.

**Primary goal**: Identify high-relevance trends before they peak and convert them into
content that positions the brand as a thought leader.
**Secondary goal**: Avoid wasting resources on declining trends, oversaturated topics,
or off-brand conversations.

## 2. Core Capabilities

- Execute a 5-step research framework (scan, filter, validate, map, brief)
- Monitor 25+ trend identification sources across platforms and industries
- Score trends on a 5-dimension validation matrix (relevance, timing, angle, risk, reach)
- Classify trends by lifecycle stage (emerging, accelerating, peak, declining, dead)
- Map validated trends to optimal content formats and platform priorities
- Analyze competitor content for gaps, patterns, and counter-positioning opportunities
- Recognize viral content patterns and extract replicable structural elements
- Execute newsjacking protocol for breaking developments
- Generate structured weekly trend briefs for the content team
- Score timing and relevance for each trend-content combination
- Monitor real-time signals for rapid-response content opportunities

## 3. When to Use This Skill

Activate this skill when any of the following conditions are true:

- The weekly content planning cycle begins (every Monday or per schedule)
- A breaking industry event requires rapid-response content evaluation
- Engagement rates are declining and fresh topic angles are needed
- The weekly brief needs trend intelligence to populate campaign topics
- Competitor content analysis is required for strategic positioning
- A new product launch needs to be connected to relevant industry conversations
- The content calendar has gaps that need data-driven topic suggestions
- The strategist node is processing research tasks in the content graph

## 4. Detailed Workflow

### Step 1: Trend Scanning (30-45 minutes)

Systematically sweep all sources from the Trend Identification Sources list (Section 6).
For each source, capture:

| Field              | Description                                           |
|--------------------|-------------------------------------------------------|
| Topic              | The trend or topic in 5-10 words                      |
| Source              | Where it was found                                    |
| Signal strength     | Weak / Moderate / Strong                              |
| First spotted       | Date the trend first appeared                         |
| Current velocity    | Accelerating / Steady / Decelerating                  |
| Related keywords    | 3-5 search terms associated with this trend           |

**Scanning protocol:**
1. Start with real-time sources (X trending, Google Trends, Hacker News)
2. Move to community sources (Reddit, Discord, Slack communities)
3. Check industry publications and newsletters
4. Review competitor feeds and recent posts
5. Scan academic/research sources for deep tech trends
6. Log all candidates in a raw trends list (aim for 15-30 candidates)

### Step 2: Trend Filtering (15-20 minutes)

Apply the Quick Filter to reduce 15-30 candidates to 5-8 shortlisted trends.

**Quick Filter (all three must be "yes" to pass):**
1. Can we connect this to our products, mission, or audience's pain points?
2. Is there a non-obvious angle we can take (not just repeating the headline)?
3. Is the trend still in the emerging or accelerating phase (not peak/declining)?

Discard any trend that fails even one filter criterion.

### Step 3: Trend Validation (20-30 minutes)

Score each shortlisted trend on the Trend Validation Matrix:

| Dimension   | Score 1 (Low)                       | Score 3 (Medium)                    | Score 5 (High)                        | Weight |
|-------------|-------------------------------------|-------------------------------------|---------------------------------------|--------|
| Relevance   | Tangential to our space             | Related to our industry             | Directly tied to our products/mission | 30%    |
| Timing      | Already peaked or declining         | At peak but still active            | Early stage, accelerating             | 25%    |
| Angle       | Only obvious takes are available    | One unique angle exists             | Multiple original angles possible     | 20%    |
| Risk        | High controversy or brand risk      | Some risk, manageable with care     | No meaningful brand risk              | 15%    |
| Reach       | Niche interest (< 1K discussions)   | Moderate interest (1K-50K)          | Broad interest (50K+ discussions)     | 10%    |

**Scoring:**
- Multiply each dimension score by its weight
- Sum for a weighted total (max 5.0)
- Trends scoring 3.5+ are validated
- Trends scoring 2.5-3.5 are conditional (need a strong angle to justify)
- Trends scoring below 2.5 are rejected

### Step 4: Trend-to-Content Mapping (15-20 minutes)

For each validated trend, determine the optimal content format, platform, and angle
using the Trend-to-Content Mapping Table (Section 8).

Fill out the mapping template for each trend:

```
Trend: [trend name]
Lifecycle stage: [emerging / accelerating / peak]
Content format: [thread / opinion post / tutorial / hot take / explainer / comparison]
Primary platform: [LinkedIn / X / TikTok / Facebook]
Secondary platform: [optional]
Angle: [our specific take in 1 sentence]
Hook concept: [draft opening line]
Urgency: [publish within 24h / this week / anytime this month]
```

### Step 5: Weekly Trend Brief Assembly (15 minutes)

Compile all validated, mapped trends into a structured Weekly Trend Brief
(template in Section 13). This brief feeds directly into the content graph's
weekly_brief.yaml configuration.

**Total estimated time per cycle: 95-130 minutes**

## 5. Research Methodology: The 5-Layer Framework

Research quality depends on checking multiple signal layers, not just surface-level
trending topics. Apply all five layers for thorough research:

| Layer | Name              | What to Look For                              | Time Budget |
|-------|-------------------|-----------------------------------------------|-------------|
| 1     | Real-Time Pulse   | What's trending RIGHT NOW across platforms     | 10 min      |
| 2     | Community Signal   | What practitioners are discussing organically  | 15 min      |
| 3     | Industry Voice     | What analysts, journalists, and VCs are saying | 10 min      |
| 4     | Competitor Watch   | What competitors are posting and what's working| 10 min      |
| 5     | Deep Signal        | Academic papers, patent filings, job postings  | 10 min      |

**Why all five layers matter:**
- Layer 1 alone gives you trending topics but no depth or differentiation
- Layer 2 reveals what real users care about vs. what media is hyping
- Layer 3 provides authority signals and emerging narratives
- Layer 4 shows content gaps you can exploit
- Layer 5 catches trends 3-6 months before they hit mainstream

## 6. Trend Identification Sources (25+ Sources)

### Layer 1: Real-Time Pulse

| #  | Source                    | URL                                    | Best For                          | Check Frequency |
|----|---------------------------|----------------------------------------|-----------------------------------|-----------------|
| 1  | Google Trends             | https://trends.google.com              | Search volume velocity            | Daily           |
| 2  | X/Twitter Trending        | https://x.com/explore/tabs/trending    | Real-time conversation spikes     | 2x daily        |
| 3  | Hacker News Front Page    | https://news.ycombinator.com           | Tech community consensus          | Daily           |
| 4  | Product Hunt              | https://www.producthunt.com            | New product launches and tools    | Daily           |
| 5  | Exploding Topics          | https://explodingtopics.com            | Early trend detection algorithms  | Weekly          |

### Layer 2: Community Signal

| #  | Source                    | URL                                        | Best For                          | Check Frequency |
|----|---------------------------|--------------------------------------------|-----------------------------------|-----------------|
| 6  | Reddit r/MachineLearning  | https://reddit.com/r/MachineLearning       | ML research trends                | Daily           |
| 7  | Reddit r/LocalLLaMA       | https://reddit.com/r/LocalLLaMA            | Open-source LLM trends            | Daily           |
| 8  | Reddit r/LangChain        | https://reddit.com/r/LangChain             | Agent/RAG framework trends        | 2x weekly       |
| 9  | Reddit r/artificial       | https://reddit.com/r/artificial            | General AI discourse              | 2x weekly       |
| 10 | Discord (Hugging Face)    | https://discord.gg/huggingface             | Model release discussions         | Weekly          |
| 11 | Discord (LangChain)       | https://discord.gg/langchain               | Framework adoption signals        | Weekly          |
| 12 | Stack Overflow Trending    | https://stackoverflow.com/questions?tab=Trending | Developer pain point trends | Weekly       |
| 13 | GitHub Trending            | https://github.com/trending                | Open-source adoption velocity     | Daily           |

### Layer 3: Industry Voice

| #  | Source                    | URL                                        | Best For                          | Check Frequency |
|----|---------------------------|--------------------------------------------|-----------------------------------|-----------------|
| 14 | TechCrunch AI             | https://techcrunch.com/category/artificial-intelligence/ | Funding and launch announcements | Daily |
| 15 | The Verge AI              | https://www.theverge.com/ai-artificial-intelligence | Consumer AI news            | Daily           |
| 16 | MIT Technology Review     | https://www.technologyreview.com           | Deep tech analysis                | Weekly          |
| 17 | a]6z Blog                 | https://a16z.com/blog/                     | VC perspective on AI markets      | Weekly          |
| 18 | The Batch (Andrew Ng)     | https://www.deeplearning.ai/the-batch/     | ML industry newsletter            | Weekly          |
| 19 | Import AI Newsletter      | https://importai.substack.com              | Policy + research trends          | Weekly          |
| 20 | Ben's Bites               | https://bensbites.beehiiv.com              | AI product ecosystem              | Daily           |

### Layer 4: Competitor Watch

| #  | Source                    | URL                                        | Best For                          | Check Frequency |
|----|---------------------------|--------------------------------------------|-----------------------------------|-----------------|
| 21 | Competitor LinkedIn feeds | (manually configured per brand)            | Content strategy patterns         | 2x weekly       |
| 22 | Competitor X feeds        | (manually configured per brand)            | Real-time positioning             | Daily           |
| 23 | SimilarWeb / Semrush      | https://www.similarweb.com                 | Traffic and keyword trends        | Monthly         |
| 24 | Competitor blog/changelog | (manually configured per brand)            | Product direction signals         | Weekly          |

### Layer 5: Deep Signal

| #  | Source                    | URL                                        | Best For                          | Check Frequency |
|----|---------------------------|--------------------------------------------|-----------------------------------|-----------------|
| 25 | ArXiv CS.AI               | https://arxiv.org/list/cs.AI/recent        | Research frontier                 | 2x weekly       |
| 26 | ArXiv CS.CL               | https://arxiv.org/list/cs.CL/recent        | NLP/LLM research                  | 2x weekly       |
| 27 | Papers With Code          | https://paperswithcode.com/trending        | Benchmark-breaking research       | Weekly          |
| 28 | Google Scholar Alerts     | https://scholar.google.com/scholar_alerts  | Keyword-triggered papers          | As triggered    |
| 29 | LinkedIn Job Postings     | (search by role/skill keywords)            | Hiring signals = investment areas | Monthly         |

## 7. Trend Lifecycle Analysis

### Lifecycle Stages

```
[Emerging] -> [Accelerating] -> [Peak] -> [Declining] -> [Dead/Evergreen]
   10%           30%             40%        15%              5%
```

| Stage        | Characteristics                                  | Content Strategy                          | Risk Level |
|--------------|--------------------------------------------------|-------------------------------------------|------------|
| Emerging     | < 500 discussions, niche communities only        | Be first. Publish explainers and predictions. Establish authority. | Low risk, high reward if trend materializes |
| Accelerating | 500-10K discussions, mainstream tech media picks up | Publish deep analysis, comparisons, tutorials. Differentiate from surface takes. | Low-medium risk |
| Peak         | 10K+ discussions, every competitor is posting    | Only post if you have a genuinely unique angle. Otherwise, skip. | Medium risk (saturation) |
| Declining    | Discussion volume dropping 20%+ week-over-week  | Publish retrospectives and "lessons learned." Counter-narrative pieces. | Low reward |
| Dead/Evergreen | Minimal new discussion, stable search volume   | Only reference as supporting context in other posts. Do not lead with it. | No risk, no reward |

### How to Determine Lifecycle Stage

1. **Check Google Trends** for the topic: Is the curve rising, flat, or falling?
2. **Count discussions** on Reddit, X, and Hacker News in the past 7 days
3. **Check competitor coverage**: If 3+ direct competitors have posted about it, it's likely at Peak
4. **Look for "backlash" signals**: Contrarian takes and "is X overhyped?" posts indicate Peak or early Decline
5. **Check news cycle age**: If the triggering event is > 5 days old, assume Peak unless data says otherwise

## 8. Trend-to-Content Mapping Table

| Trend Type              | Best Content Format    | Platform Priority      | Urgency       | Example                                    |
|-------------------------|------------------------|------------------------|---------------|--------------------------------------------|
| Breaking product launch | Hot take + analysis    | X first, LinkedIn 2nd  | Same day      | "GPT-5 just dropped. Here's what changes." |
| New framework/library   | Tutorial + comparison  | LinkedIn + TikTok      | Within 3 days | "I migrated from X to Y. Here's my honest take." |
| Industry debate         | Opinion post           | LinkedIn primary       | Within 5 days | "The open-source vs. closed-source AI debate misses the point." |
| Viral meme/format       | Adapted version        | X + TikTok             | Same day      | "[Meme format] but for [our industry]"     |
| Research paper          | Explainer thread       | X thread + LinkedIn    | Within 7 days | "This paper changes how we think about [topic]. Thread:" |
| Funding announcement    | Market analysis        | LinkedIn primary       | Within 2 days | "Company X raised $100M for [space]. What it means for [audience]." |
| Regulatory/policy       | Impact analysis        | LinkedIn + X           | Same day      | "The EU AI Act enforcement starts [date]. Here's what you need to do." |
| Hiring surge            | Industry insight       | LinkedIn primary       | Within 7 days | "[Company] is hiring 200 ML engineers. Here's what that signals." |
| Open-source release     | First-look review      | X + TikTok             | Within 2 days | "I spent 4 hours with [new tool]. Honest review:" |
| Conference keynote      | Key takeaway summary   | X (real-time), LinkedIn| Same day      | "5 things from [conference] that matter for [audience]:" |

## 9. Competitor Content Analysis Framework

### Step-by-Step Competitor Analysis

**Step 1: Identify 5-8 direct competitors and 3-5 adjacent brands**

Direct competitors = same product category.
Adjacent brands = different product but same audience.

**Step 2: Audit their last 30 days of content across all platforms**

For each competitor, capture:

| Metric                  | How to Measure                                      |
|-------------------------|-----------------------------------------------------|
| Posting frequency       | Posts per week per platform                         |
| Top-performing posts    | Sort by engagement; note top 5                      |
| Content themes          | Categorize each post by topic (product, thought leadership, meme, etc.) |
| Formats used            | Text, image, video, carousel, thread, poll          |
| Engagement patterns     | Which types get most comments vs. shares vs. likes  |
| Gaps and weaknesses     | Topics they ignore, platforms they underinvest in   |
| Tone and positioning    | Formal vs. casual, expert vs. peer, corporate vs. human |

**Step 3: Build the Competitive Content Map**

```
            High Engagement
                 |
    [Competitor A]    [Us - target]
                 |
  Serious -------+------- Playful
                 |
    [Competitor B]    [Competitor C]
                 |
            Low Engagement
```

Position yourself in a quadrant that's either unoccupied or underserved.

**Step 4: Identify Content Gaps**

Content gaps = topics your audience cares about that NO competitor is covering well.
These are your highest-opportunity content plays.

Common gap categories:
- Technical depth (competitors stay surface-level)
- Practitioner perspective (competitors post from corporate voice)
- Specific use cases (competitors speak generically)
- Behind-the-scenes transparency (competitors only share polished narratives)
- Counter-narrative (everyone says X, nobody says "but what about Y?")

## 10. Viral Content Pattern Recognition

### The 7 Viral Content Archetypes

| # | Archetype              | Structure                                          | Why It Spreads                        |
|---|------------------------|----------------------------------------------------|---------------------------------------|
| 1 | The Revelation         | "I discovered X. It changes everything about Y."   | Curiosity gap + transformation promise|
| 2 | The Contrarian         | "Everyone says X. Here's why they're wrong."        | Identity + debate trigger             |
| 3 | The Quantified Story   | "I did X for N days/months. Here are the numbers."  | Proof + voyeurism + benchmark         |
| 4 | The Curation           | "N best [resources/tools/tips] for [audience]."     | Save-worthy utility value             |
| 5 | The Behind-the-Curtain | "Here's how we actually [built/failed/decided] X."  | Exclusivity + authenticity            |
| 6 | The Framework          | "Use this [matrix/flowchart/template] for X."       | Actionable + shareable + saveable     |
| 7 | The Prediction         | "Here's what happens to [industry] in [timeframe]." | Debate trigger + thought leadership   |

### Pattern Extraction Protocol

When you find a viral post (10x+ normal engagement for that account), dissect it:

1. **Hook**: What is the first line? How many characters? What emotion does it trigger?
2. **Structure**: How is the body organized? (Numbered list, story arc, problem-solution)
3. **Value density**: How much actionable information per 100 words?
4. **Emotional arc**: Does it follow tension-release, revelation, or escalation?
5. **CTA placement**: Where is the call to action? What type is it?
6. **Visual element**: Is there an image, video, or is it text-only?
7. **Timing**: When was it posted? What was happening in the news cycle?

Document this in the viral pattern library for reuse.

## 11. Newsjacking Protocol

### When to Newsjack

Newsjacking = inserting your brand into a breaking news story with a relevant angle.

**Decision flowchart:**

```
Breaking event detected
    |
    v
Is it relevant to our audience? -- No --> Skip
    |
    Yes
    v
Can we add unique insight (not just react)? -- No --> Skip
    |
    Yes
    v
Is there brand risk in commenting? -- High --> Skip (or legal review)
    |
    Low/None
    v
Can we publish within 4 hours? -- No --> Write a next-day analysis instead
    |
    Yes
    v
EXECUTE NEWSJACK
```

### Newsjacking Execution Steps

1. **Draft in 30 minutes**: Speed matters more than perfection. Aim for 80% quality.
2. **Lead with the news, pivot to your angle**: "X just happened. Here's what it means for [audience]."
3. **Add original analysis**: Data, personal experience, technical breakdown. Not just "wow, big news."
4. **Publish on X first**: Fastest distribution. Cross-post to LinkedIn within 2 hours.
5. **Monitor and reply**: Newsjack posts get high visibility. Be ready for volume.

### Newsjacking Timing

| Timing           | Content Type           | Engagement Potential |
|------------------|------------------------|---------------------|
| 0-2 hours        | Hot take / first reaction | Highest (10-50x)   |
| 2-8 hours        | Analysis with context  | High (5-20x)       |
| 8-24 hours       | Deep dive / tutorial   | Medium (3-10x)     |
| 24-72 hours      | Retrospective / lessons| Low-medium (2-5x)  |
| 72+ hours        | Too late for newsjack  | Baseline            |

## 12. Platform-Specific Research Guidelines

### LinkedIn Research

- Monitor "LinkedIn Top Voices" in your category for topic signals
- Check LinkedIn News sidebar daily for editorial picks
- Track trending LinkedIn hashtags via the search bar
- Watch for LinkedIn newsletter launches by competitors
- LinkedIn polls reveal what the audience is thinking about (check competitors' polls)

### X (Twitter) Research

- Use advanced search operators: `(keyword1 OR keyword2) min_faves:100 -is:retweet`
- Monitor Lists of industry leaders (create private lists of 50-100 key voices)
- Track Spaces conversations for emerging discussion topics
- Watch quote-tweet threads for debate topics
- Use Nitter or RSS feeds for systematic monitoring without algorithmic filtering

### TikTok Research

- Search keywords in the Discover tab to see trending sounds and formats
- Monitor the For You page for format innovations relevant to your niche
- Track trending sounds that could be adapted for educational/professional content
- Watch competitor TikToks for engagement patterns (comment volume vs. view count ratios)
- Check TikTok Creative Center for trending hashtags and creator insights

### Facebook Research

- Monitor relevant Facebook Groups for organic discussion topics
- Check Facebook Watch for trending video formats in your category
- Track competitor Pages for post frequency and engagement patterns
- Use CrowdTangle (if available) for viral content detection
- Monitor Facebook News for editorial trend signals

## 13. Quality Checklist

Before submitting the Weekly Trend Brief, verify every item:

- [ ] All 5 research layers have been scanned (real-time, community, industry, competitor, deep)
- [ ] At least 15 raw trend candidates were identified before filtering
- [ ] Each shortlisted trend passes the 3-question Quick Filter
- [ ] Each validated trend has a Validation Matrix score of 3.5+
- [ ] Trend lifecycle stage is identified and documented for each trend
- [ ] Content format and platform mapping is complete for each trend
- [ ] At least one emerging-stage trend is included (future positioning)
- [ ] No more than one peak-stage trend is included (avoid saturation)
- [ ] Competitor analysis has been refreshed within the last 7 days
- [ ] Newsjacking candidates are flagged with urgency levels
- [ ] Each trend has a proposed angle that differentiates from competitor coverage
- [ ] Timing and urgency recommendations are realistic given team capacity
- [ ] Sources are documented for traceability and follow-up monitoring

## 14. Output Format Template

### Weekly Trend Brief (JSON)

```json
{
  "brief_date": "2026-03-28",
  "analyst": "strategist_agent",
  "research_time_minutes": 115,
  "raw_candidates_scanned": 23,
  "validated_trends": [
    {
      "trend_name": "Local LLM deployment surpasses cloud API usage",
      "lifecycle_stage": "accelerating",
      "validation_score": 4.2,
      "relevance_score": 5,
      "timing_score": 4,
      "angle_score": 4,
      "risk_score": 5,
      "reach_score": 3,
      "sources": [
        "Reddit r/LocalLLaMA (3 front-page posts this week)",
        "Hacker News discussion (482 points)",
        "Google Trends (+140% 90-day)"
      ],
      "proposed_angle": "Our platform enables local deployment -- share real benchmarks vs. cloud",
      "content_mapping": {
        "format": "comparison_post_with_data",
        "primary_platform": "linkedin",
        "secondary_platform": "x_thread",
        "urgency": "this_week",
        "hook_concept": "We ran the same model locally vs. cloud for 30 days. The cost difference will shock you."
      },
      "competitor_coverage": "2 of 5 competitors have posted about this, both surface-level"
    }
  ],
  "newsjacking_candidates": [
    {
      "event": "Major cloud provider announces LLM API price increase",
      "relevance": "high",
      "urgency": "within_24_hours",
      "proposed_angle": "This is why local-first matters. Here's the math."
    }
  ],
  "content_gaps_identified": [
    "No competitor has published actual local vs. cloud benchmark data",
    "Tutorial content for non-ML-engineers running local models is missing"
  ],
  "next_week_watch": [
    "EU AI Act enforcement date approaching -- regulatory content opportunity",
    "Llama 4 community benchmarks expected -- first-look review opportunity"
  ]
}
```

## 15. Complete Examples

### Example 1: Trend Research Leading to LinkedIn Post

**Research finding:**
- Source: Reddit r/LocalLLaMA + Hacker News
- Trend: "Ollama passes 1M weekly active users"
- Lifecycle: Accelerating
- Validation score: 4.4
- Competitor coverage: 1 of 5 competitors mentioned it (repost only, no analysis)

**Content mapping:**
- Format: Data-backed opinion post
- Platform: LinkedIn (primary), X thread (secondary)
- Angle: Connect to broader "local AI" movement; position our tools as part of ecosystem
- Urgency: This week

**Resulting LinkedIn post:**
```
The local AI revolution just hit a milestone most people missed.

Ollama crossed 1 million weekly active users last week.

Why this matters more than any funding announcement:

1. It proves developers want to OWN their AI stack, not rent it
2. Privacy isn't a "nice to have" anymore -- it's a deployment requirement
3. The cost math finally favors local: $0.002/query vs. $0.03/query for GPT-4 class models

We've been building for this moment. Our platform runs on Ollama
under the hood, and here's what our users are seeing:

- 93% cost reduction vs. cloud APIs
- 0ms cold start (no network round trip)
- Full data sovereignty (nothing leaves the machine)

But here's the question I keep coming back to:

Will local-first AI become the default in 2 years,
or will cloud providers adjust pricing to stay competitive?

I see arguments both ways. What's your read?
```

**Why the research made this post better:**
- Specific data point (1M users) from community sources, not just opinion
- Positioned ahead of competitors (only 1 had mentioned it, without analysis)
- Connected trending topic directly to product value proposition
- Used research to add credibility ("$0.002/query vs. $0.03/query")

### Example 2: Newsjacking on X

**Research finding:**
- Source: X Trending + TechCrunch (Layer 1 + Layer 3)
- Event: "OpenAI announces 3x API price increase effective next month"
- Lifecycle: Breaking (< 2 hours old)
- Newsjacking decision: Yes (relevant, unique angle, low risk, can publish fast)

**X thread (published within 90 minutes of announcement):**
```
Tweet 1:
OpenAI just raised API prices 3x.

Here's what nobody is talking about:
This makes local LLMs the obvious choice for 80% of production use cases.

Let me show you the math. Thread:

Tweet 2:
Current GPT-4o cost: ~$0.03 per 1K tokens
New GPT-4o cost: ~$0.09 per 1K tokens

Running Llama 4 locally on a $2K GPU:
~$0.001 per 1K tokens (electricity only after hardware)

Breakeven: 6 weeks of moderate usage.

Tweet 3:
"But local models aren't as good!"

For 80% of tasks (classification, extraction, summarization, RAG),
local models match or beat cloud APIs.

The 20% where GPT-4+ truly wins? Keep using cloud for those.
Run everything else locally.

Tweet 4:
We built our entire platform around this thesis.

Today's announcement validates what we've been saying for 12 months:

The future of AI is hybrid. Cloud for cutting edge. Local for everything else.

Here's our benchmark comparison (updated today): [link in reply]

Tweet 5:
If you're evaluating local deployment, here's where to start:

1. Ollama for local model serving (free, 5-minute setup)
2. Our platform for production orchestration
3. Llama 4 or Mistral as your base model

Reply with your use case -- I'll recommend the right setup.
```

**Timing result:** Published 90 minutes after announcement. Got 340 retweets
(vs. account average of 12) because of first-mover advantage with substantive analysis.

## 16. Common Mistakes

| Mistake | Why It's Bad | Better Approach |
|---------|-------------|-----------------|
| Chasing every trending topic | Dilutes brand positioning. Audience can't tell what you stand for. You burn team capacity on low-ROI content. | Filter ruthlessly. Only pursue trends scoring 3.5+ on the validation matrix AND connecting to your core narrative. |
| Reporting news without analysis | Zero differentiation. Your post adds nothing that a Google search wouldn't provide. Algorithm rewards original analysis. | Always add one of: original data, personal experience, unique framework, actionable takeaway, or contrarian angle. |
| Posting about declining trends | Content arrives after audience has moved on. Engagement will be below baseline. Makes brand look slow. | Check lifecycle stage BEFORE committing to content creation. Declining trends get retrospectives at most, not primary coverage. |
| Copying competitor content angles | Audience sees the same take from multiple accounts and ignores all of them. You look derivative. | Use competitor analysis to find gaps, not inspiration. Ask "what are they NOT saying?" instead of "what are they saying?" |
| Skipping community sources (Layer 2) | Mainstream media lags community discussion by 3-7 days. You'll always be late if you only read publications. | Reddit, Discord, and GitHub trending are your early warning system. Prioritize these in daily scans. |
| No research documentation | Team can't learn from past research. Same trends get re-evaluated. No institutional knowledge builds. | Log every research cycle in the Weekly Trend Brief format. Review past briefs before starting new cycles. |
| Newsjacking risky topics | Brand association with controversial events can cause lasting damage that no engagement spike is worth. | Apply the newsjacking decision flowchart strictly. When in doubt, skip. There will always be another opportunity. |
| Ignoring deep signals (Layer 5) | ArXiv papers and patent filings predict trends 3-6 months early. Ignoring them means you're always reacting, never leading. | Dedicate 10 minutes per research cycle to Layer 5 sources. You only need to catch 1-2 early signals per month. |
| Over-indexing on Google Trends | Google Trends shows search volume, not content opportunity. High search volume often means oversaturated content. | Use Google Trends as ONE input, cross-referenced with community discussion volume and competitor coverage density. |
| Researching without a time box | Research can expand infinitely. Diminishing returns hit hard after 2 hours. Team burns time that should go to content creation. | Strict 2-hour time box per research cycle. Use the step-by-step workflow with time budgets from Section 4. |

## 17. Advanced Techniques

### Trend Triangulation

Never validate a trend from a single source. Require signals from at least 2 of the
5 research layers before investing content resources:

- Layer 1 + Layer 2 = "confirmed active trend" (real-time + community validation)
- Layer 2 + Layer 5 = "early deep trend" (community buzz + research foundation)
- Layer 1 + Layer 3 = "media-driven trend" (may be hype; validate with Layer 2)
- Layer 4 + Layer 2 = "competitive opportunity" (competitors covering what community wants)

Single-layer signals are hypotheses, not validated trends.

### Counter-Trend Positioning

When a trend reaches Peak stage, the highest-value content play is often the
counter-narrative:

1. Identify the consensus take ("Everyone says X is the future")
2. Find the legitimate counter-evidence (limitations, edge cases, failed implementations)
3. Position as "Here's what the hype is missing" -- not "X is bad"
4. Support with data or personal experience to avoid seeming contrarian for its own sake

Counter-trend content at Peak stage gets 3-5x engagement vs. consensus content
because it triggers debate and feels novel in a saturated conversation.

### Predictive Trend Modeling

Use the following signals to predict which emerging trends will accelerate:

| Signal                              | Predictive Power | Where to Find It            |
|-------------------------------------|------------------|-----------------------------|
| GitHub stars growth rate > 50%/month | Strong           | GitHub Trending, Star History|
| Job postings mentioning the technology doubled QoQ | Strong | LinkedIn Jobs, Indeed  |
| VC funding in the space > $500M in 90 days | Strong   | Crunchbase, TechCrunch      |
| 3+ ArXiv papers citing the approach in 30 days | Medium | ArXiv, Semantic Scholar     |
| Major tech company blog post or announcement | Medium  | Company engineering blogs   |
| Conference talk acceptances trending up | Medium       | Conference programs          |
| Subreddit subscriber growth > 20%/month | Moderate    | Subreddit Stats              |

When 3+ strong signals align, the trend will almost certainly accelerate.
Publish content immediately to establish first-mover positioning.

### Seasonal Trend Calendar

Some trends are cyclical. Build a 12-month calendar of predictable content opportunities:

| Month   | Predictable Trends                                    | Content Play                          |
|---------|-------------------------------------------------------|---------------------------------------|
| January | "Year ahead" predictions, New Year resolutions for tech | Prediction posts, tool roundups      |
| March   | End of Q1 reflections, budget cycle starts            | ROI analysis posts, cost comparison   |
| May     | Google I/O, Microsoft Build                           | Conference coverage, analysis         |
| June    | CVPR, mid-year reviews                                | Research roundups, trend check-ins    |
| Sept    | Back to work energy, new project season               | Tutorial content, getting-started guides |
| Oct     | Hacktoberfest, open-source momentum                   | Open-source contribution content      |
| Nov     | AWS re:Invent, Black Friday for tools                 | Cloud vs. local cost analysis         |
| Dec     | Year in review, predictions for next year             | Retrospective content, prediction posts |

## 18. Settings and Configuration

The trend-researcher skill is configured via the weekly brief and environment settings:

```yaml
# In config/weekly_brief.yaml
research_settings:
  research_cycle_frequency: "weekly"       # weekly | biweekly | daily
  time_budget_minutes: 120                 # Maximum time per research cycle
  min_validation_score: 3.5                # Minimum trend validation score
  min_raw_candidates: 15                   # Minimum trends to scan before filtering
  max_validated_trends: 5                  # Maximum trends to include in brief
  lifecycle_preference: "emerging"         # emerging | accelerating | any
  newsjacking_enabled: true                # Enable rapid-response newsjacking
  newsjacking_max_hours: 4                 # Maximum hours after event to newsjack
  competitor_refresh_days: 7               # Days between full competitor analysis
  deep_signal_enabled: true                # Include Layer 5 (ArXiv, patents) research

  # Competitor list
  competitors:
    direct:
      - "competitor_a_handle"
      - "competitor_b_handle"
    adjacent:
      - "adjacent_brand_handle"

  # Keyword watchlist (triggers alerts across all sources)
  keywords:
    - "local LLM"
    - "AI agents"
    - "RAG pipeline"
    - "open source AI"
    - "LangGraph"
    - "Ollama"
```

Per-campaign research override:

```yaml
campaigns:
  - name: "Product Launch Week"
    research_settings:
      newsjacking_enabled: false           # Don't newsjack during launch (stay on message)
      lifecycle_preference: "accelerating" # Only ride established trends during launch
      max_validated_trends: 3              # Focus on fewer, higher-confidence trends
```

## 19. Notes

- Research quality degrades without consistency. Run the full 5-step framework every
  cycle, even when time-pressured. Shortcuts compound into blind spots.
- The strategist agent should execute this skill BEFORE any content creation begins
  in the weekly cycle. Trend intelligence feeds the weekly_brief.yaml which drives
  all downstream nodes.
- Trend validation scores are relative to your specific brand and audience. A trend
  scoring 3.0 for a general tech brand might score 5.0 for a specialized AI
  infrastructure company. Calibrate weights based on your positioning.
- Newsjacking is high-reward but requires speed. If you cannot publish within 4 hours
  of a breaking event, switch to a "next-day analysis" format instead. Late hot takes
  are worse than no hot take.
- Layer 5 (deep signals) has the highest long-term value but the lowest immediate
  payoff. Resist the temptation to skip it during busy weeks. One early trend
  detection per quarter can drive months of differentiated content.
- All sources in Section 6 should be reviewed quarterly. Sources go stale, new platforms
  emerge, and community energy migrates. Update the source list as part of quarterly
  strategy reviews.
- The competitor list in Settings should be reviewed monthly. New entrants appear,
  companies pivot, and the competitive landscape shifts faster in AI than any other
  sector.
- Research documentation is an investment, not overhead. Past Weekly Trend Briefs
  become a searchable knowledge base that accelerates future research cycles and
  prevents redundant analysis.
