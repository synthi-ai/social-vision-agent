---
name: visual-branding
description: Generate consistent visual prompts and image descriptions that align with tech brand identity. Activate for visual content creation.
license: MIT
metadata:
  agents: "visual"
  category: creative
---

# Visual Branding Skill

## 1. Overview

The Visual Branding skill ensures every image, graphic, and visual element produced
by the content pipeline maintains a cohesive brand identity across all platforms. This
skill governs two primary outputs: (1) image generation prompts sent to AI image tools,
and (2) image descriptions and alt-text for accessibility and SEO.

In the Social Vision Agents architecture, the visual node sits between the writer node
and the optimizer node. It receives written content and enriches it with visual direction
-- either matching provided image URLs from `config/weekly_brief.yaml` to content, or
generating detailed prompts for image creation.

This skill activates whenever the pipeline needs visual content: social media post images,
carousel slides, thread graphics, thumbnail designs, or any visual element that will
carry the brand's identity.

## 2. Core Capabilities

- Define and enforce a consistent brand color palette with hex codes and usage ratios
- Apply typography hierarchy across visual content types
- Select appropriate visual themes based on content category and platform
- Generate structured image prompts using the 5-component SSMCC framework
- Enforce platform-specific image dimensions and format requirements
- Create accessible visuals with proper contrast ratios and alt-text
- Design carousel sequences with visual narrative flow
- Optimize thumbnail images for click-through rate
- Maintain visual consistency across multi-platform campaigns
- Build mood boards by content type for reference and consistency
- Apply do/don't rules to prevent off-brand visual decisions

## 3. When to Use This Skill

Activate the visual-branding skill when ANY of these conditions are true:

| Trigger Condition | Example |
|---|---|
| Post requires an accompanying image | Any social media post in the pipeline |
| `weekly_brief.yaml` includes `image_url` | Campaign provides image assets |
| Thread needs visual tweets | Image placement at strategic positions |
| Carousel/slideshow content | LinkedIn carousel, TikTok slideshow |
| Thumbnail needed for video content | TikTok, YouTube Shorts cross-posts |
| Alt-text generation required | Accessibility compliance for all images |
| New visual asset being created | Blog header, social card, infographic |
| Brand consistency audit triggered | Periodic review of visual output |

Do NOT activate for:
- Text-only posts with no visual component
- Reposts/quote-tweets without added media
- Posts that explicitly specify `media: none` in the campaign config

## 4. Detailed Workflow

### Step 1: Determine Visual Requirements

Read the content from the writer node and the campaign configuration to determine:

1. **Platform**: Which platform(s) will display this image?
2. **Content type**: Post image, carousel slide, thread visual, thumbnail?
3. **Image source**: Provided URL from weekly_brief.yaml or needs generation?
4. **Mood alignment**: What emotion should the image evoke?
5. **Text overlay**: Does the image need text overlay (carousel) or standalone?

### Step 2: Apply Brand Color Palette

#### Primary Palette

| Color | Hex | RGB | Usage | Ratio |
|---|---|---|---|---|
| Deep Navy | #1a1a2e | 26, 26, 46 | Backgrounds, primary surfaces | 35% |
| Electric Purple | #6c63ff | 108, 99, 255 | CTAs, accents, highlights | 20% |
| Pure White | #ffffff | 255, 255, 255 | Text on dark, breathing space | 25% |
| Soft Gray | #e8e8e8 | 232, 232, 232 | Secondary text, borders | 10% |

#### Accent Palette

| Color | Hex | RGB | Usage | Ratio |
|---|---|---|---|---|
| Cyan Glow | #00d4ff | 0, 212, 255 | Data highlights, tech accents | 5% |
| Warm Orange | #ff6b35 | 255, 107, 53 | Alerts, urgent CTAs, contrast pops | 3% |
| Success Green | #00c853 | 0, 200, 83 | Positive metrics, checkmarks | 2% |

#### Background System

| Context | Background Color | Text Color | Contrast Ratio |
|---|---|---|---|
| Dark mode (default) | #0d0d1a | #ffffff | 17.4:1 |
| Light mode (LinkedIn) | #f5f5f7 | #1a1a2e | 14.8:1 |
| Gradient hero | #1a1a2e -> #6c63ff | #ffffff | 12.1:1 min |
| Code block | #0d0d1a | #00d4ff (keywords) | 10.2:1 |
| Accent card | #6c63ff | #ffffff | 5.8:1 |

**Rule**: Never use brand colors below a 4.5:1 contrast ratio for text. This is
the WCAG AA minimum. Aim for 7:1 or higher (WCAG AAA) whenever possible.

### Step 3: Apply Typography Hierarchy

#### Font Stack

| Level | Font Style | Weight | Size (relative) | Use Case |
|---|---|---|---|---|
| H1 / Title | Clean sans-serif (Inter, Helvetica Neue) | Bold (700) | 1.8rem | Carousel title slides, hero images |
| H2 / Subtitle | Clean sans-serif | Semi-bold (600) | 1.3rem | Section headers in carousels |
| Body | Clean sans-serif | Regular (400) | 1rem | Body text in image overlays |
| Caption | Clean sans-serif | Light (300) | 0.85rem | Source credits, dates |
| Code | Monospace (JetBrains Mono, Fira Code) | Regular (400) | 0.9rem | Code snippets, terminal output |
| Data / Stat | Clean sans-serif | Extra-bold (800) | 2.5rem | Large numbers in infographics |

#### Typography Rules

1. Never use more than 2 font weights in a single image
2. Minimum text size on mobile: 14px equivalent (nothing smaller)
3. Line height for text overlays: 1.5x font size
4. Letter spacing for ALL CAPS headings: +2% tracking
5. Maximum 3 text hierarchy levels per image (title, body, caption)
6. Code text always uses monospace, never the body font

### Step 4: Select Visual Theme

Match the content type to the appropriate visual theme:

#### Theme 1: Abstract Tech

**When to use**: AI/ML content, architecture discussions, future-looking posts
**Elements**: Neural network nodes, flowing data particles, connected mesh,
gradient orbs, circuit-like patterns
**Mood**: Innovative, sophisticated, cutting-edge
**Colors**: Deep Navy + Cyan Glow + Electric Purple

```
Visual reference:
- Softly glowing interconnected nodes on dark background
- Gradient light trails suggesting data flow
- Geometric patterns with depth-of-field blur
- Abstract 3D shapes with glass/frosted material
```

#### Theme 2: Developer Workspace

**When to use**: Tutorials, tool recommendations, coding content, behind-the-scenes
**Elements**: Clean desk with monitor, terminal/code on screen, mechanical keyboard,
dark IDE with syntax-highlighted code
**Mood**: Focused, productive, authentic
**Colors**: Deep Navy background + syntax highlighting colors

```
Visual reference:
- Over-the-shoulder view of code on a dark IDE
- Split-screen: code on left, result on right
- Minimal desk with single monitor, warm ambient lighting
- Terminal window with green/cyan text on black
```

#### Theme 3: Future-Forward

**When to use**: Product announcements, vision posts, industry predictions
**Elements**: Gradients, glass morphism panels, subtle 3D floating elements,
holographic effects, light flares
**Mood**: Optimistic, bold, aspirational
**Colors**: Electric Purple + Warm Orange + Cyan Glow gradients

```
Visual reference:
- Frosted glass cards floating on gradient background
- 3D product mockups with subtle shadow and reflection
- Neon accent lines on minimal dark surfaces
- Layered transparent shapes with depth
```

#### Theme 4: Data & Evidence

**When to use**: Case studies, benchmark results, comparisons, data-driven posts
**Elements**: Clean charts, minimal graphs, before/after comparisons, metric cards
**Mood**: Credible, clear, authoritative
**Colors**: Deep Navy + Success Green + Warm Orange (for contrast data)

```
Visual reference:
- Bar chart with one bar highlighted in brand color
- Side-by-side comparison cards with check/x icons
- Dashboard-style metric cards with large numbers
- Line graph showing improvement trajectory
```

### Step 5: Generate Image Prompt (SSMCC Framework)

Every image generation prompt must include all five components:

| Component | Description | Example |
|---|---|---|
| **S**ubject | The primary focus of the image | "A minimal LangGraph node diagram with 8 connected nodes" |
| **S**tyle | The artistic approach | "Clean flat design with subtle 3D depth, tech illustration style" |
| **M**ood | The emotional tone | "Professional yet innovative, quietly confident" |
| **C**olors | Specific hex codes or descriptive palette | "Deep navy (#1a1a2e) background, electric purple (#6c63ff) node highlights, cyan (#00d4ff) connection lines" |
| **C**omposition | Layout and framing | "Center-focused with negative space on edges, 16:9 aspect ratio, main subject filling 60% of frame" |

#### Prompt Assembly Template

```
[Subject]: {detailed description of the primary subject and any secondary elements}
[Style]: {artistic style, rendering approach, visual reference}
[Mood]: {emotional tone, energy level, atmosphere}
[Colors]: {specific hex codes mapped to elements, overall color temperature}
[Composition]: {layout, aspect ratio, rule of thirds placement, negative space}

Additional: {platform-specific requirements, text safe zones, mobile-viewing considerations}
```

#### Example Prompts by Theme

**Abstract Tech prompt:**
```
Subject: An interconnected network of 8 glowing nodes arranged in a flowing
left-to-right graph structure, with data particles flowing along the edges
between nodes. Each node is a different size representing its importance.

Style: Modern tech illustration, soft glow effects, subtle depth-of-field
blur on background elements. Clean vector-inspired shapes with slight 3D
dimensionality. No photorealism.

Mood: Innovative and sophisticated. The image should feel like looking at
a living system -- active but controlled, complex but understandable.

Colors: Background deep navy (#0d0d1a). Nodes in electric purple (#6c63ff)
with soft outer glow. Connection lines in cyan (#00d4ff) at 60% opacity.
Data particles as small white (#ffffff) dots with motion blur.

Composition: 16:9 landscape. Graph flows from left-center to right-center.
Main cluster of nodes positioned at rule-of-thirds intersection. Left 20%
and right 15% left as negative space for potential text overlay. Bottom
10% clear for platform UI elements.
```

**Developer Workspace prompt:**
```
Subject: A close-up over-the-shoulder view of a developer's monitor showing
a Python code editor with syntax-highlighted LangGraph code. The code is
visible but intentionally slightly blurred to emphasize atmosphere over
readability. A minimal desk with a mechanical keyboard in the foreground.

Style: Photorealistic with cinematic color grading. Shallow depth of field
with the monitor in focus and foreground keyboard softly blurred. Warm
ambient lighting from the left side.

Mood: Focused and productive. Late evening coding session energy -- calm
concentration, the satisfying feeling of building something that works.

Colors: Monitor displays dark IDE theme with deep navy (#1a1a2e) background,
purple (#6c63ff) keywords, cyan (#00d4ff) strings, white (#ffffff) text.
Ambient room lighting warm orange (#ff6b35) from a desk lamp, creating
contrast with the cool monitor glow.

Composition: 16:9 landscape. Monitor fills upper 70% of frame, angled
slightly left. Keyboard visible in lower 20%. Right edge shows soft
bokeh of a secondary monitor. Rule of thirds: code center-right.
```

### Step 6: Validate Platform Dimensions

Before finalizing any visual, verify it matches the target platform spec.

#### Platform Dimension Reference

| Platform | Post Image | Carousel / Slide | Story / Reel | Profile Header |
|---|---|---|---|---|
| **LinkedIn** | 1200x627 (1.91:1) or 1080x1080 (1:1) | 1080x1350 (4:5) | 1080x1920 (9:16) | 1584x396 (4:1) |
| **X / Twitter** | 1600x900 (16:9) or 1200x675 (16:9) | N/A (thread images) | N/A | 1500x500 (3:1) |
| **TikTok** | 1080x1080 (1:1) | 1080x1920 (9:16) | 1080x1920 (9:16) | N/A |
| **Facebook** | 1200x630 (1.91:1) | 1080x1080 (1:1) | 1080x1920 (9:16) | 820x312 (2.63:1) |

#### File Format Requirements

| Format | Max Size | Use Case | Notes |
|---|---|---|---|
| JPEG | 5 MB (X), 10 MB (LinkedIn) | Photos, complex images | Quality 85-92% for best size/quality |
| PNG | 5 MB (X), 10 MB (LinkedIn) | Graphics with text, screenshots | Use for sharp text overlays |
| WebP | 5 MB | Modern platforms | Better compression, check support |
| GIF | 15 MB (X) | Animations | Lower engagement than static in threads |
| PDF | 100 MB (LinkedIn) | Carousels on LinkedIn | Up to 300 slides (10 recommended) |

### Step 7: Write Alt-Text

Every image must include descriptive alt-text for accessibility. Alt-text serves
both screen reader users and SEO discovery.

#### Alt-Text Formula

```
[What the image shows] + [Key data or text in the image] + [Context for why it matters]
```

#### Alt-Text Rules

1. Length: 80-150 characters (concise but descriptive)
2. Never start with "Image of..." or "Picture of..." (screen readers already say "image")
3. Include any text visible in the image verbatim
4. Mention data values shown in charts or graphs
5. Describe the visual hierarchy: what should the viewer see first?
6. Do not include hashtags or promotional language in alt-text

#### Alt-Text Examples

**Good:**
```
"LangGraph architecture diagram showing 8 nodes: researcher, strategist,
product_expert, writer, visual, optimizer, human_approval, publisher,
connected by conditional edges in a left-to-right flow."
```

**Bad:**
```
"Image of our cool architecture. Check it out! #AI #LangGraph"
```

**Good:**
```
"Bar chart comparing inference costs: Ollama Llama 4 at $0 per call
versus GPT-4o at $0.03 per call, showing 100x cost difference over
30,000 monthly API calls."
```

**Bad:**
```
"Cost comparison chart"
```

## 5. Frameworks and Models

### The Visual Consistency Matrix

Ensure every visual output scores positively on all five dimensions:

| Dimension | Question to Ask | Failure Indicator |
|---|---|---|
| **Color fidelity** | Are only brand palette colors used? | Any color not in the palette |
| **Typography** | Does text follow the hierarchy? | Mixed weights, wrong fonts |
| **Theme alignment** | Does the visual match the content theme? | Abstract tech on a lifestyle post |
| **Platform fit** | Are dimensions and format correct? | Wrong aspect ratio, oversized file |
| **Accessibility** | Does contrast meet WCAG AA (4.5:1)? | Light text on light background |

### The 60-30-10 Color Rule

For any single image:
- **60%** dominant color (usually Deep Navy or background)
- **30%** secondary color (usually White or Soft Gray for content)
- **10%** accent color (Electric Purple, Cyan Glow, or Warm Orange for emphasis)

This ratio creates visual harmony. Violating it produces chaotic, off-brand images.

### Visual Weight Hierarchy

Elements should draw the eye in this order:
1. **Primary focal point**: The main subject (largest, highest contrast)
2. **Supporting data**: Statistics, labels, annotations (medium size, brand accent)
3. **Background context**: Patterns, textures, ambient elements (lowest contrast)

If background elements compete with the focal point, reduce their opacity or blur them.

## 6. Platform-Specific Visual Guidelines

### LinkedIn

**Visual strategy**: Professional, clean, authoritative. LinkedIn users scan feeds
quickly on desktop -- images must communicate value in under 2 seconds.

**Best performing visual types:**
1. Data visualization with one key stat highlighted (2.3x avg engagement)
2. Before/after comparison cards (1.8x avg engagement)
3. Clean quote cards with attribution (1.6x avg engagement)
4. Carousel posts with 6-10 slides (3.2x avg engagement vs single image)

**Carousel design system:**
- Slide 1 (Cover): Bold title + hook question on brand gradient background
- Slides 2-8 (Content): One key point per slide, consistent layout
- Slide 9 (Summary): Recap of 3-5 key takeaways
- Slide 10 (CTA): "Follow [profile] for more" + logo + handle

**Layout template per carousel slide:**
```
+----------------------------------+
|  [Brand color bar - 8px top]     |
|                                  |
|  HEADLINE TEXT                   |
|  (Inter Bold, 36px, #ffffff)     |
|                                  |
|  Body text explaining the point  |
|  in 2-3 concise sentences.       |
|  (Inter Regular, 20px, #e8e8e8)  |
|                                  |
|  +----------------------------+  |
|  |  Visual element: icon,     |  |
|  |  chart, or illustration    |  |
|  +----------------------------+  |
|                                  |
|  Slide 3/10    @handle           |
+----------------------------------+
```

**LinkedIn-specific rules:**
- Use light mode color scheme (white/light gray background) for higher readability
  in the LinkedIn feed, which is predominantly white
- Include your handle or logo subtly on every slide (bottom-right, small)
- Text on images: minimum 20px equivalent, high contrast
- Avoid stock photography aesthetics (staged handshakes, generic office shots)

### X / Twitter

**Visual strategy**: Bold, high-contrast, mobile-first. 80% of X users browse on
mobile -- every visual must be legible on a 6-inch screen.

**Best performing visual types:**
1. Code screenshots with syntax highlighting (2.1x avg engagement for tech audience)
2. Charts with one surprising data point highlighted (1.9x avg)
3. Memes using brand colors and fonts (2.8x avg when appropriate)
4. Annotated screenshots of products or tools (1.7x avg)

**Thread-specific image placement:**
- Image at position 3 or 4: Peak attention, use your most informative visual
- Image at position N-2: Re-engagement visual, use your most surprising data
- Never use images at position 1 (competing with text hook) or position 2 (too early)

**X-specific rules:**
- Use 16:9 aspect ratio (1600x900) for maximum feed real estate
- Dark mode friendly: test how your image looks on both light and dark X feeds
- Text on images: minimum 24px equivalent (mobile readability)
- Code screenshots: use a tool like Carbon or ray.so with dark theme
- Memes: only when the brand voice supports it and the joke is genuinely funny

### TikTok

**Visual strategy**: Vibrant, dynamic, thumb-stopping. TikTok is a vertical-first
platform where static images compete with video for attention.

**Best performing visual types:**
1. Carousel slideshows with bold text (primary format for non-video content)
2. Screen recordings with text overlays (tutorial style)
3. "Duet-ready" images with reaction space on the side
4. Text-heavy infographics in 9:16 vertical format

**TikTok carousel design:**
- Vertical format: 1080x1920 (9:16)
- Maximum 35 slides (optimal: 5-8 for engagement)
- Large text: minimum 32px equivalent (thumb-scrolling viewing distance)
- High saturation: TikTok's audience responds to vibrant, energetic colors
- Movement cues: arrows, numbered sequences that invite swiping

**TikTok-specific rules:**
- Increase accent color usage to 15-20% (more vibrant than other platforms)
- Use Warm Orange (#ff6b35) more prominently (high visibility on mobile)
- Bottom 15% of vertical images should be clear (covered by TikTok UI)
- Top 10% should be clear (covered by status bar and profile icons)
- Safe zone for text: middle 75% of the image

### Facebook

**Visual strategy**: Warm, community-focused, shareable. Facebook's algorithm
favors images that generate comments and shares, not just likes.

**Best performing visual types:**
1. Infographics with clear takeaways (2.4x share rate vs plain images)
2. Photo-style images with warm color grading (1.7x engagement)
3. Multi-image albums telling a sequential story (1.9x engagement)
4. Quote cards with relatable statements (2.1x share rate)

**Album/multi-image design:**
- Image 1 (Cover): Sets context, displayed largest in the feed
- Images 2-4: Supporting details, displayed as grid below cover
- Consistent aspect ratio across all images (1200x630 recommended)
- Visual continuity: same color scheme and style across the album

**Facebook-specific rules:**
- Warm color temperature: shift the palette slightly warmer for Facebook
- Community-oriented imagery: people, collaboration, connection (even abstract)
- Text overlay: Facebook's old 20% text rule is gone, but images with less
  text still perform better in ad reach
- Link preview images: when a link is shared, the OG image is 1200x630;
  ensure brand consistency in those assets too

## 7. Quality Checklist

Before submitting any visual output to the optimizer node, verify:

- [ ] Colors are exclusively from the brand palette (no rogue colors)
- [ ] 60-30-10 color ratio is maintained
- [ ] Text contrast meets WCAG AA minimum (4.5:1 ratio)
- [ ] Typography follows the defined hierarchy (max 2 weights per image)
- [ ] Image dimensions match the target platform specification
- [ ] File size is under the platform limit
- [ ] Alt-text is written (80-150 characters, descriptive, no "Image of...")
- [ ] Visual theme matches the content type
- [ ] Text on images is legible at mobile viewing size (minimum 20px LinkedIn, 24px X, 32px TikTok)
- [ ] Safe zones are respected (no critical content in platform UI overlay areas)
- [ ] Brand handle or logo is subtly present on carousel slides
- [ ] Image works in both light and dark mode contexts (test both)
- [ ] No stock photography aesthetics (generic, staged, overly polished)
- [ ] Visual focal point is immediately clear (viewer knows where to look first)
- [ ] Prompt includes all 5 SSMCC components if image generation is needed

## 8. Output Format Template

The visual node should output image specifications in the following JSON structure:

```json
{
  "visual_id": "uuid-v4",
  "post_id": "linked-post-uuid",
  "platform": "linkedin",
  "image_type": "carousel",
  "source": "provided_url",
  "image_url": "https://cdn.example.com/graph-architecture.png",
  "dimensions": {
    "width": 1080,
    "height": 1350,
    "aspect_ratio": "4:5"
  },
  "theme": "abstract_tech",
  "color_usage": {
    "dominant": "#1a1a2e",
    "secondary": "#ffffff",
    "accent": "#6c63ff"
  },
  "alt_text": "LangGraph architecture diagram showing 8 nodes connected by conditional edges, with researcher on the left flowing to publisher on the right",
  "text_overlays": [
    {
      "text": "Production AI Agent Architecture",
      "font_weight": 700,
      "size_px": 36,
      "color": "#ffffff",
      "position": "top-left"
    },
    {
      "text": "8 nodes. 0 hallucinations.",
      "font_weight": 400,
      "size_px": 20,
      "color": "#e8e8e8",
      "position": "center"
    }
  ],
  "generation_prompt": null,
  "carousel_sequence": {
    "slide_number": 3,
    "total_slides": 10,
    "has_consistent_layout": true
  },
  "accessibility": {
    "contrast_ratio_main_text": 17.4,
    "contrast_ratio_secondary_text": 14.8,
    "wcag_level": "AAA"
  },
  "metadata": {
    "campaign_id": "weekly_brief_2026_w13",
    "content_pillar": "technical_credibility",
    "visual_theme": "abstract_tech"
  }
}
```

When image generation is needed (no URL provided), the `generation_prompt` field
contains the full SSMCC prompt:

```json
{
  "generation_prompt": {
    "subject": "Interconnected network of 8 glowing nodes in a left-to-right graph structure with data particles flowing along edges",
    "style": "Modern tech illustration, soft glow effects, vector-inspired shapes with slight 3D dimensionality",
    "mood": "Innovative and sophisticated, active but controlled",
    "colors": "Background #0d0d1a, nodes #6c63ff with outer glow, connections #00d4ff at 60% opacity, particles #ffffff",
    "composition": "16:9 landscape, graph centered, 20% negative space left for text overlay, bottom 10% clear",
    "full_prompt": "[assembled prompt string from components above]"
  }
}
```

## 9. Complete Examples

### Example 1: LinkedIn Carousel -- Before and After

**BEFORE (inconsistent branding):**
```
Slide 1: Stock photo of handshake, red and blue colors, generic "AI Solutions" title
Slide 2: White background, small black text, no visual hierarchy
Slide 3: Different font from slide 1, green accent color (not in palette)
Slide 4: "Follow us!" with clip-art thumbs up icon
```

Problems: Off-brand colors, stock photography, inconsistent fonts, no visual system,
clip-art, generic messaging, only 4 slides.

**AFTER (on-brand visual system):**
```
Slide 1 (Cover):
  Background: Gradient from #1a1a2e to #6c63ff (left to right)
  Title: "How We Built Production AI Agents" (Inter Bold, 36px, #ffffff)
  Subtitle: "7 Lessons from 6 Months of LangGraph" (Inter Regular, 20px, #e8e8e8)
  Bottom: @handle (Inter Light, 14px, #e8e8e8, right-aligned)

Slide 2 (Context):
  Background: #1a1a2e solid
  Header: "The Problem" (Inter Bold, 28px, #ff6b35)
  Body: "Linear agent pipelines break in production. Every. Single. Time."
  (Inter Regular, 22px, #ffffff)
  Visual: Simple line diagram showing a broken pipeline (red X)
  Footer: 2/10 @handle

Slide 3 (Architecture):
  Background: #1a1a2e solid
  Header: "The Solution: Graph Architecture" (Inter Bold, 28px, #6c63ff)
  Visual: Clean node diagram with 8 labeled nodes in brand purple
  Connections: Cyan (#00d4ff) lines between nodes
  Footer: 3/10 @handle

Slides 4-8 (Lessons):
  [Consistent layout: header in accent color, body in white, one
   supporting icon or mini-chart per slide, footer with pagination]

Slide 9 (Summary):
  Background: #1a1a2e solid
  Header: "Key Takeaways" (Inter Bold, 28px, #00d4ff)
  Bullet list with checkmark icons in Success Green (#00c853)
  5 one-line takeaways in Inter Regular, 20px, #ffffff

Slide 10 (CTA):
  Background: Gradient #6c63ff to #1a1a2e
  Text: "Follow for weekly AI engineering insights" (Inter Bold, 28px, #ffffff)
  Handle: @handle (Inter Bold, 24px, #00d4ff)
  Subtle brand logo bottom-right
```

### Example 2: X/Twitter Thread Image -- Before and After

**BEFORE (weak visual):**
```
A generic screenshot of a code editor with tiny, unreadable text.
No brand colors visible. JPEG compression artifacts. No alt-text.
Light theme IDE that washes out in the X timeline.
```

**AFTER (on-brand visual):**
```
Image spec:
  Dimensions: 1600x900 (16:9)
  Format: PNG for sharp text rendering

  Content: Carbon.sh code screenshot showing Python LangGraph node
  definition. Dark theme with custom colors:
    - Background: #0d0d1a (brand Deep Navy)
    - Keywords: #6c63ff (brand Electric Purple)
    - Strings: #00d4ff (brand Cyan Glow)
    - Comments: #e8e8e8 (brand Soft Gray)
    - Functions: #ff6b35 (brand Warm Orange)

  Carbon settings:
    - Theme: Custom (brand colors above)
    - Font: JetBrains Mono, 16px
    - Padding: 32px
    - Window controls: visible (adds authenticity)
    - Line numbers: on

  Annotation:
    - Small callout arrow pointing to the key line of code
    - Callout text: "This is where the magic happens"
    - Callout style: #ff6b35 background, #ffffff text, rounded corners

  Alt-text: "Python code showing a LangGraph node function that wraps
  the LLM call in error recovery, with a try/except block that routes
  to a recovery node on failure. Key line highlighted: recovery_node
  decides retry, skip, or escalate."
```

## 10. Common Mistakes

| Mistake | Why It's Bad | Better Approach |
|---|---|---|
| Using colors outside the brand palette | Breaks visual consistency; audience can't build pattern recognition | Only use defined palette hex codes; create tints by adjusting opacity |
| Stock photography with generic subjects | Feels inauthentic; signals "we didn't invest in this" | Custom illustrations, real screenshots, or branded graphics |
| Tiny text on images (under 16px) | Illegible on mobile where 80% of social media is consumed | Minimum 20px LinkedIn, 24px X, 32px TikTok |
| Inconsistent fonts across carousel slides | Looks unprofessional; breaks the visual system | Use only the defined font stack; set up slide templates |
| Ignoring platform dimension specs | Images get cropped awkwardly, cutting off key content | Always verify dimensions against the platform reference table |
| No alt-text on images | Excludes screen reader users; misses SEO value | Write 80-150 char alt-text for every image |
| Text in platform UI overlay zones | Critical content hidden behind likes/comments/UI | Respect safe zones: bottom 15% TikTok, top 10% TikTok |
| Same image across all platforms | Wrong aspect ratios; mismatched visual expectations | Create platform-specific versions from a master design |
| Low contrast text overlays | Fails WCAG accessibility; hard to read in bright sunlight | Minimum 4.5:1 contrast ratio; prefer 7:1 or higher |
| Overloading images with information | Viewer doesn't know where to look; cognitive overload | One focal point per image; use visual weight hierarchy |
| Using GIFs in X threads | Lower impression reach than static images in thread context | Use static PNG/JPEG in threads; save GIFs for standalone tweets |
| Ignoring dark mode rendering | Images with thin borders disappear on dark backgrounds | Test all images in both light and dark mode feeds |

## 11. Advanced Techniques

### Visual A/B Testing Framework

When the campaign allows, create two visual variants for the same post:

| Variant | Change | Metric to Track |
|---|---|---|
| A (Control) | Standard brand visual | Impressions, engagement rate |
| B (Test) | Single variable change | Same metrics, compare after 48 hours |

Testable variables (change only one per test):
- Background color (dark vs light)
- Accent color (purple vs cyan vs orange)
- Image style (illustration vs screenshot vs data viz)
- Text overlay (with vs without)
- Aspect ratio (16:9 vs 1:1 on platforms that support both)

### Dynamic Color Temperature by Content Pillar

Shift the accent color emphasis based on content type:

| Content Pillar | Primary Accent | Rationale |
|---|---|---|
| Technical credibility | Cyan Glow (#00d4ff) | Cool, precise, data-oriented |
| Product showcase | Electric Purple (#6c63ff) | Premium, innovative, brand-forward |
| Community / Culture | Warm Orange (#ff6b35) | Approachable, energetic, human |
| Thought leadership | Deep Navy + White | Authoritative, clean, trustworthy |

### Carousel Narrative Patterns

**The Revelation:** Slides build suspense toward a key insight on slide 7-8.
Each slide adds one more piece of context until the full picture emerges.

**The Comparison:** Alternating slides: Approach A / Approach B, with a verdict
slide at the end. Side-by-side layout within each comparison slide.

**The Countdown:** "10 tools..." starting from #10. Descending order creates
anticipation. The #1 tool gets a double-slide treatment with more detail.

**The Journey:** Chronological. Start with "Where we were" and end with "Where
we are now." Use consistent left-to-right visual flow across slides.

### Thumbnail Optimization

For video content (TikTok, YouTube Shorts cross-posts), thumbnails determine CTR:

1. **Face rule**: Thumbnails with expressive human faces get 30% higher CTR
2. **Text limit**: Maximum 4 words on a thumbnail (must be readable at 120px wide)
3. **Contrast**: Thumbnail must pop against adjacent content in the feed
4. **Curiosity gap**: Show the setup but not the result (e.g., "Before" side
   of a before/after, with "After" hidden)
5. **Brand mark**: Subtle brand color frame or corner logo for recognition

### Mood Board by Content Type

Maintain reference mood boards for visual consistency:

| Content Type | Mood Board Elements | Energy Level |
|---|---|---|
| Tutorial | Code screenshots, step arrows, numbered badges, terminal windows | Calm, focused |
| Case Study | Before/after splits, metric cards, timeline graphics, growth charts | Evidence-based |
| Product Launch | 3D mockups, gradient backgrounds, glass morphism, light effects | High energy |
| Opinion / Hot Take | Bold typography, single accent color, minimal graphics | Direct, confident |
| Behind the Scenes | Authentic workspace photos, candid style, warm lighting | Relaxed, genuine |
| Data Analysis | Clean charts, highlight colors, annotation callouts, comparison grids | Analytical |

## 12. Settings and Configuration

### weekly_brief.yaml Visual Configuration

```yaml
campaigns:
  - name: "AI Agents Deep Dive"
    visual_config:
      theme: "abstract_tech"
      color_temperature: "cool"
      primary_accent: "#00d4ff"
      images:
        - url: "https://cdn.example.com/graph-architecture.png"
          alt_text: "LangGraph 8-node architecture diagram"
          platforms:
            linkedin:
              dimensions: "1080x1350"
              format: "carousel_slide"
            x_twitter:
              dimensions: "1600x900"
              format: "thread_image"
            tiktok:
              dimensions: "1080x1920"
              format: "carousel_vertical"
      generate_variants: false
      text_overlays_enabled: true
```

### Visual Node Parameters

The visual node in `src/graph/nodes.py` accepts these parameters via graph state:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `theme` | str | "abstract_tech" | Visual theme to apply |
| `color_mode` | str | "dark" | "dark" or "light" background mode |
| `primary_accent` | str | "#6c63ff" | Primary accent hex code |
| `text_overlay` | bool | true | Whether to include text on images |
| `generate_alt_text` | bool | true | Whether to generate alt-text |
| `carousel_slides` | int | 10 | Number of slides for carousel format |
| `safe_zone_margin` | float | 0.1 | Fraction of image to keep clear for UI |
| `contrast_minimum` | float | 4.5 | Minimum contrast ratio for text |
| `prompt_style` | str | "ssmcc" | Prompt framework to use |

### Brand Asset References

Maintain a `/config/brand/` directory with:

```
config/brand/
  palette.yaml        # Hex codes, RGB, usage ratios
  typography.yaml     # Font families, weights, sizes
  themes/
    abstract_tech.yaml
    developer_workspace.yaml
    future_forward.yaml
    data_evidence.yaml
  templates/
    carousel_linkedin.yaml
    thread_image_x.yaml
    vertical_tiktok.yaml
  mood_boards/
    tutorial.yaml
    case_study.yaml
    product_launch.yaml
```

## 13. Notes

- Images are provided via URLs in `config/weekly_brief.yaml`, NOT generated by the
  pipeline. The visual node's job is to validate, describe, and optimize provided
  images -- not to create them from scratch. Generation prompts are output for
  potential future use or external image creation workflows.
- The visual node should store image metadata in PostgreSQL (`posts` table) with
  the visual specification embedded in the post record.
- When Groq is used as the LLM fallback instead of Ollama, alt-text generation
  quality tends to be comparable, but prompt generation may need additional
  formatting constraints.
- Contrast ratio calculations: use the WCAG relative luminance formula:
  `L = 0.2126 * R + 0.7152 * G + 0.0722 * B` (where R, G, B are linearized).
  Ratio = `(L1 + 0.05) / (L2 + 0.05)` where L1 is the lighter color.
- For carousel PDFs uploaded to LinkedIn, ensure each slide is exported at 150 DPI
  minimum for crisp text rendering on retina displays.
- The optimizer node should validate visual output against this skill's checklist
  before passing to human_approval. Flag any checklist failures as warnings in
  the graph state.
- When repurposing visuals across platforms, never just resize. Re-compose the
  layout for each platform's aspect ratio and safe zones. A 16:9 image cropped
  to 9:16 will always look wrong.
