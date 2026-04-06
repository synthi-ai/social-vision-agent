---
name: hashtag-strategy
description: Select high-performing, platform-appropriate hashtags that maximize
  reach without looking spammy. Activate when generating or optimizing hashtags.
license: MIT
metadata:
  agents: "writer,optimizer"
  category: optimization
---

# Hashtag Strategy Skill

## 1. Overview

This skill governs hashtag selection, placement, and optimization across all
social media platforms. It provides the writer and optimizer agents with a
systematic methodology for choosing hashtags that extend reach, target the
right audiences, and comply with platform-specific limits and conventions.

Activate this skill whenever hashtags are generated, reviewed, or optimized
as part of the content pipeline.

## 2. Core Capabilities

- 3-tier hashtag model (broad, niche, branded) for balanced reach
- Platform-specific limit enforcement (hard caps per platform)
- Hashtag research methodology for trending and evergreen tags
- Competition density analysis (high vs. low competition tags)
- CamelCase formatting enforcement for readability
- Banned and flagged hashtag detection
- Multilingual hashtag considerations
- Placement optimization (inline vs. end of post)
- Weekly hashtag rotation to avoid staleness
- Performance tracking and iteration

## 3. When to Use This Skill

| Trigger | Action |
|---------|--------|
| Writer agent generates hashtags for any post | Apply 3-tier model and platform limits |
| Optimizer agent reviews hashtags | Validate limits, check banned list, optimize placement |
| Weekly brief includes trending topics | Research matching hashtags |
| Post targets a new audience segment | Adjust tier 2 niche hashtags |
| Engagement data shows hashtag underperformance | Rotate underperforming tags |

## 4. Detailed Workflow

### Step 1: Identify the Post's Core Topics

Extract 3-5 core topics from the post content. These drive hashtag selection.

Example post about AI-powered farm logistics:
- Core topics: AI, agriculture, logistics, supply chain, technology

### Step 2: Apply the 3-Tier Hashtag Model

For every post, combine hashtags from three tiers:

**Tier 1: Broad (1-2 per post)**
High-volume, generic tags that cast a wide net. These have millions of posts
but expose your content to the largest possible audience.

Characteristics:
- 1M+ posts on the platform
- Single-word or very common phrases
- High competition, low conversion
- Purpose: discovery by new audiences

Examples: #AI, #Tech, #Startup, #Developer, #Agriculture, #Innovation

Selection criteria:
- Must be directly relevant to the post's primary topic
- Must not be so broad as to be meaningless (#love, #instagood)
- Limit to 1-2 per post to avoid diluting niche targeting

**Tier 2: Niche (2-3 per post)**
Medium-volume, targeted tags specific to your domain. These are where most
engagement comes from — the audience is smaller but highly relevant.

Characteristics:
- 10K-1M posts on the platform
- Multi-word compound phrases
- Medium competition, high relevance
- Purpose: reaching your actual target audience

Examples: #AIAgents, #MLOps, #LocalFirstAI, #DevTools, #AgriTech,
#FarmToTable, #SupplyChainTech, #PrecisionAgriculture

Selection criteria:
- Must describe your specific niche or sub-topic
- Should match terms your target audience actually searches for
- Rotate 50% of niche tags weekly to test new audiences
- Use CamelCase for multi-word tags (#LocalFirstAI not #localfirstai)

**Tier 3: Branded (0-1 per post)**
Your own brand-specific tags for community building and content tracking.

Characteristics:
- Low volume (you create the volume)
- Unique to your brand or campaign
- Zero competition (you own them)
- Purpose: community building, campaign tracking, content aggregation

Examples: #BuildWithFarmsConnect, #FarmsConnectStories, #AgriTechWeekly

Selection criteria:
- Only include when the post is brand-forward or part of a campaign
- Must be memorable and easy to spell
- Don't force branded tags on every post — reserve for signature content
- Track branded tag adoption by community members as a success metric

### Step 3: Enforce Platform Limits

| Platform | Min | Max | Optimal | Placement |
|----------|-----|-----|---------|-----------|
| LinkedIn | 2 | 5 | 3-4 | End of post, after blank line |
| X | 1 | 3 | 1-2 | Inline or end of tweet |
| TikTok | 3 | 8 | 5-6 | In caption, after CTA |
| Facebook | 1 | 4 | 2-3 | End of post |

**Hard rule:** Never exceed the platform maximum. Exceeding limits looks
spammy and can trigger algorithm penalties.

**Placement rules by platform:**

**LinkedIn:**
```
[Post body]

[CTA question]

#Hashtag1 #Hashtag2 #Hashtag3
```
Hashtags go at the very end, separated from the CTA by a blank line.
Never put hashtags inline in LinkedIn posts.

**X:**
```
[Tweet body with #InlineTag if natural]

#EndTag1 #EndTag2
```
One hashtag can go inline if it reads naturally in the sentence.
Remaining hashtags go at the end. Total: 1-3.

**TikTok:**
```
[Caption text]

[CTA]

#tag1 #tag2 #tag3 #tag4 #tag5 #trending
```
TikTok is the only platform where 5-8 hashtags is acceptable.
Mix evergreen niche tags with trending tags.

**Facebook:**
```
[Post body and CTA]

#Hashtag1 #Hashtag2
```
Minimal hashtags. Facebook audiences don't search by hashtag as much.
2-3 is the sweet spot.

### Step 4: Research Trending Hashtags

For each weekly batch, research current trending hashtags:

1. **Platform search:** Type core topics into each platform's search bar
   and note the suggested hashtags and their post volumes
2. **Competitor analysis:** Check what hashtags top competitors and industry
   leaders are using this week
3. **Trending topics:** Cross-reference with Twitter trends, TikTok Discover,
   and LinkedIn trending topics
4. **Seasonal relevance:** Check for seasonal or event-specific tags
   (#HarvestSeason, #CES2026, #WorldFoodDay)

### Step 5: Validate Hashtag Quality

Before including any hashtag, run these checks:

| Check | Question | Action if Fail |
|-------|----------|----------------|
| Relevance | Does this tag directly relate to the post content? | Remove it |
| Volume | Does this tag have enough posts to matter (>1K)? | Replace with higher-volume alternative |
| Banned check | Is this tag flagged or shadow-banned on the platform? | Remove immediately |
| Competition | Is this tag so saturated that content gets buried? | Downgrade to tier 2 niche variant |
| Readability | Is the tag easy to read and understand? | Apply CamelCase or shorten |
| Brand safety | Could this tag associate with unwanted content? | Remove and find alternative |

### Step 6: Apply CamelCase Formatting

All multi-word hashtags must use CamelCase for accessibility and readability:

| Wrong | Right |
|-------|-------|
| #localfirstai | #LocalFirstAI |
| #farmtotable | #FarmToTable |
| #supplychaintech | #SupplyChainTech |
| #machinelearning | #MachineLearning |

CamelCase is not just a style preference — screen readers read CamelCase
hashtags as separate words, making content accessible to visually impaired users.

### Step 7: Weekly Rotation Strategy

To avoid hashtag fatigue and test new audiences:

- **Keep constant (weekly):** Tier 1 broad tags + branded tags
- **Rotate 50% (weekly):** Tier 2 niche tags
- **Always fresh:** Trending and seasonal tags

Track which niche tags drive the most impressions and engagement over 4-week
cycles. Promote high-performers to "always use" status. Drop underperformers.

## 5. Frameworks and Models

### The Hashtag Pyramid

```
        /\
       /  \   Tier 3: Branded (0-1)
      /    \  Your brand, your campaign
     /------\
    /        \   Tier 2: Niche (2-3)
   /          \  Your specific domain
  /------------\
 /              \   Tier 1: Broad (1-2)
/                \  Wide reach, general topics
```

### Competition Density Matrix

| Density | Post Volume | Strategy |
|---------|-------------|----------|
| Ultra-high | 10M+ | Avoid as primary — your post gets buried in seconds |
| High | 1M-10M | Use 1 max, pair with niche tags for balance |
| Medium | 100K-1M | Sweet spot — good reach with reasonable visibility window |
| Low | 10K-100K | Great for niche targeting, higher engagement rate |
| Micro | <10K | Only if highly relevant — limited discovery potential |

### Hashtag Effectiveness Formula

```
Effectiveness = (Relevance × Reach) / Competition
```

- **Relevance (1-10):** How closely does the tag match the post content?
- **Reach (log scale):** How many people follow or search this tag?
- **Competition (1-10):** How many posts compete for visibility under this tag?

High relevance + medium reach + low competition = best performing hashtags.

## 6. Platform-Specific Guidelines

### 6.1 LinkedIn Hashtag Strategy

**Optimal count:** 3-4 hashtags
**Placement:** End of post, after blank line separator

**LinkedIn-specific rules:**
- LinkedIn shows hashtag followers — use tags with 10K+ followers
- Company page hashtags (up to 3 chosen by admin) boost reach for brand posts
- LinkedIn algorithm weights the first 3 hashtags most heavily
- Industry-specific hashtags outperform generic tech tags on LinkedIn
- Follow your own hashtags to monitor community usage

**High-performing LinkedIn hashtag categories:**
- Industry: #AgriTech, #FoodTech, #SupplyChain
- Role: #Founders, #CTO, #ProductManagement
- Topic: #AIAgents, #BuildInPublic, #StartupLessons
- Community: #LinkedInCreators, #TechCommunity

### 6.2 X Hashtag Strategy

**Optimal count:** 1-2 hashtags
**Placement:** Inline (if natural) or end of tweet

**X-specific rules:**
- Fewer hashtags = more engagement on X (tweets with 1-2 tags outperform 3+)
- Hashtags count toward the 280-character limit
- Trending hashtags can boost visibility dramatically but only if relevant
- Thread tweets: hashtags on tweet 1 only (not every tweet)
- Use Twitter's trending section for real-time hashtag opportunities

**X hashtag strategy for threads:**
```
Tweet 1: [Content] #Tag1 #Tag2
Tweet 2-N: [Content, no hashtags]
Last tweet: [CTA] #Tag1
```

### 6.3 TikTok Hashtag Strategy

**Optimal count:** 5-6 hashtags
**Placement:** End of caption

**TikTok-specific rules:**
- TikTok search is hashtag-driven — treat tags as SEO keywords
- Mix trending tags (check TikTok Discover) with niche tags
- #FYP, #ForYouPage, #Viral — these are controversial. Some creators report
  they help; others say they're noise. Use sparingly if at all.
- Niche-specific tags (#AgriTok, #FarmLife, #TechTok) reach better-targeted audiences
- Hashtag challenges can drive massive reach — participate when relevant

**TikTok hashtag formula:**
```
2 trending + 2 niche + 1 topic + 1 branded = 6 hashtags
```

### 6.4 Facebook Hashtag Strategy

**Optimal count:** 2-3 hashtags
**Placement:** End of post

**Facebook-specific rules:**
- Facebook hashtags are less impactful than other platforms
- Use them for content categorization, not discovery
- Group-specific hashtags can boost visibility within communities
- Never exceed 4 — Facebook audiences perceive excessive hashtags as spam
- Event and campaign hashtags work well for tracking

## 7. Quality Checklist

- [ ] Hashtag count is within platform-specific optimal range
- [ ] Does NOT exceed platform maximum under any circumstances
- [ ] Includes at least 1 tier 1 (broad) hashtag
- [ ] Includes at least 2 tier 2 (niche) hashtags
- [ ] Branded hashtag included only when appropriate (not forced)
- [ ] All multi-word hashtags use CamelCase
- [ ] No banned or flagged hashtags included
- [ ] All hashtags are directly relevant to post content
- [ ] Hashtags are placed in the correct position for the platform
- [ ] At least 50% of tier 2 tags were rotated from last week
- [ ] No duplicate hashtags within the same post
- [ ] Hashtags don't repeat the same word (e.g., #AI and #ArtificialIntelligence)
- [ ] Character count includes hashtag length (relevant for X)

## 8. Output Format Template

```json
{
  "platform": "linkedin",
  "hashtags": {
    "selected": ["#AgriTech", "#AIAgents", "#FarmToTable", "#BuildInPublic"],
    "tiers": {
      "broad": ["#AgriTech"],
      "niche": ["#AIAgents", "#FarmToTable"],
      "branded": ["#BuildInPublic"]
    },
    "placement": "end_of_post",
    "count": 4,
    "within_limit": true
  },
  "rejected": [
    {"tag": "#Innovation", "reason": "too generic, no targeting value"},
    {"tag": "#farming", "reason": "no CamelCase, too broad"}
  ],
  "rotation_notes": "Swapped #SupplyChainTech for #FarmToTable this week to test food-focused audience."
}
```

## 9. Complete Examples

### Example 1: LinkedIn Post About AI Farm Analytics

**Post topic:** AI-powered crop yield prediction tool launch

**Hashtag selection process:**

Step 1 — Core topics: AI, agriculture, crop yield, prediction, analytics

Step 2 — 3-tier selection:
- Tier 1 (broad): #AI, #AgriTech → selected #AgriTech (more targeted than #AI)
- Tier 2 (niche): #PrecisionAgriculture, #CropAnalytics, #FarmData
  → selected #PrecisionAgriculture, #CropAnalytics
- Tier 3 (branded): #FarmsConnectAI → selected

Step 3 — LinkedIn limit check: 4 tags, max 5 ✓

**Result:**
```
#AgriTech #PrecisionAgriculture #CropAnalytics #FarmsConnectAI
```

### Example 2: X Thread About Supply Chain Optimization

**Post topic:** How route optimization reduced farm delivery costs

**Hashtag selection process:**

Step 1 — Core topics: logistics, route optimization, cost reduction, farming

Step 2 — 3-tier selection:
- Tier 1 (broad): #SupplyChain
- Tier 2 (niche): #AgriLogistics → but only 2K posts, swap to #FarmTech
- No branded tag (thread is educational, not brand-forward)

Step 3 — X limit check: 2 tags, max 3 ✓

**Result (tweet 1 only):**
```
#SupplyChain #FarmTech
```

### Example 3: TikTok Video About Direct-to-Consumer Sales

**Post topic:** How farmers sell directly to restaurants

**Hashtag selection process:**

Step 1 — Core topics: direct sales, farmers, restaurants, farm-to-table, food

Step 2 — 3-tier selection:
- Tier 1 (broad): #FarmLife, #FoodTok
- Tier 2 (niche): #FarmToTable, #DirectSales, #SmallFarm
- Tier 3 (trending): #FYP (debatable, but included for reach)

Step 3 — TikTok limit check: 6 tags, max 8 ✓

**Result:**
```
#FarmLife #FoodTok #FarmToTable #DirectSales #SmallFarm #FYP
```

## 10. Common Mistakes

| Mistake | Why It's Bad | Better Approach |
|---------|-------------|-----------------|
| Using 10+ hashtags on LinkedIn | Looks spammy, algorithm may penalize | Stick to 3-5 max |
| All broad/generic tags | Post gets buried, no niche targeting | Use 3-tier model with majority niche |
| No CamelCase on compound tags | Inaccessible to screen readers, hard to read | Always CamelCase: #LocalFirstAI |
| Same hashtags every week | Audience fatigue, algorithm notices repetition | Rotate 50% of niche tags weekly |
| Hashtags in middle of LinkedIn post | Breaks reading flow, looks unnatural | Always place at end with blank line separator |
| Using banned/flagged tags | Content gets shadow-banned or hidden | Research tag status before using |
| Hashtags not matching content | Attracts wrong audience, high bounce rate | Every tag must relate to post content |
| Copying competitor tags blindly | Their audience may not be your audience | Research relevance, don't just copy |
| Ignoring character count on X | Hashtags eat into 280 char limit | Budget characters: content first, tags second |
| Using hashtags on every tweet in a thread | Looks repetitive, spammy in timeline | Hashtags on tweet 1 and last tweet only |
| Lowercase compound tags | #supplychain reads as one word, less clickable | #SupplyChain — always |
| Branded tags on every post | Forces brand presence where it's not natural | Reserve for campaign and brand-forward posts |

## 11. Advanced Techniques

### Hashtag Sets by Content Type

Pre-build hashtag sets for common content types to speed up selection:

| Content Type | Hashtag Template |
|-------------|-----------------|
| Product launch | 1 broad industry + 2 product-niche + 1 branded |
| Thought leadership | 1 broad role + 2 topic-niche + 0 branded |
| Community engagement | 1 broad community + 1 niche + 1 campaign |
| Educational thread | 1 broad topic + 1-2 niche + 0 branded |

### Hashtag A/B Testing

Post similar content with different hashtag sets to test performance:
- Set A: All niche tags (high relevance, lower reach)
- Set B: Mixed broad + niche (wider reach, lower relevance)
- Measure: impressions, engagement rate, follower growth

### Seasonal Hashtag Calendar

Maintain a calendar of seasonal and event hashtags:
- Q1: #NewYear, #CES, #TechWeek
- Q2: #PlantingSeason, #EarthDay, #SpringHarvest
- Q3: #SummerHarvest, #AgTech, #FoodSecurity
- Q4: #HarvestSeason, #WorldFoodDay, #YearInReview

### Negative Hashtag List

Maintain a blocklist of hashtags to never use:
- Currently flagged or shadow-banned tags
- Tags associated with spam or bot activity
- Tags that attract irrelevant audiences
- Tags with controversial or offensive associations
- Overly generic tags with zero targeting value (#happy, #love, #instagood)

## 12. Settings and Configuration

| Config File | What It Controls |
|-------------|-----------------|
| `config/platforms.yaml` | Hashtag limits per platform, placement rules |
| `config/weekly_brief.yaml` | Campaign-specific hashtags, trending topics |
| `config/vision.md` | Branded hashtag definitions |

**Writer agent:** Generates initial hashtag set using 3-tier model.
**Optimizer agent:** Validates limits, checks banned list, optimizes placement.

## 13. Notes

- Hashtag strategy should evolve based on performance data. After 4-8 weeks
  of tracking, you'll have enough data to identify which tags consistently
  drive impressions and engagement for your specific audience.
- Trending hashtags have a short shelf life (24-72 hours on X, 3-5 days on
  TikTok). Only use them when the content is genuinely relevant.
- When entering a new market or audience segment, research that segment's
  native hashtag vocabulary before posting. Don't assume your existing tags
  translate to new audiences.
- Accessibility is non-negotiable: CamelCase is a requirement, not a
  suggestion. Screen readers depend on it.
