# ONE-SHOT AGENT PROMPT
## پرامپت یکسره — تولید کامل یک قسمت از صفر تا تحویل

---

## قبل از استفاده — سه نکته

**۱. این پرامپت برای یک AI ایجنت واقعی نوشته شده** — یعنی ابزاری که بتواند تصویر بسازد، فایل ذخیره کند، TTS اجرا کند و خروجی بدهد. اگر ابزارت فقط چت است، از MASTER PROMPT v3 مرحله‌به‌مرحله استفاده کن؛ نتیجه بهتر می‌شود چون در هر مرحله می‌توانی اصلاح کنی.

**۲. درباره‌ی Filmora:** حالت Text/Idea to Video در Filmora می‌تواند از یک ایده، اسکریپت و استوری‌بورد صحنه‌به‌صحنه با ویژوال و دیالوگ قابل ویرایش بسازد و بعد با Seedance 2.0 یا Sora 2 یا Veo 3.1 رندر بگیرد، و خروجی را با تراک‌های جدای ویدیو، صدا و زیرنویس تحویل بدهد. ولی Filmora یک ایجنت قابل‌برنامه‌ریزی نیست — نمی‌توانی یک پرامپت بدهی و برود ۱۱ پلان با شخصیت قفل‌شده بسازد. بخش «نقشه‌ی Filmora» در انتهای این فایل، تقسیم کار واقعی را مشخص می‌کند.

**۳. هشدار لایسنس:** طبق اعلام خود Filmora، منابع تولیدشده با AI مثل text to video و افکت‌های صوتی AI به دلیل ابهام در وضعیت تجاری داده‌های آموزشی برای استفاده‌ی غیرتجاری هستند، در حالی که مثلاً موسیقی AI با برچسب «Commercially available» برای استفاده‌ی تجاری مجاز است. قبل از مانیتایز، وضعیت هر فیچری که استفاده می‌کنی را داخل نرم‌افزار چک کن.

---

## پرامپت یکسره (این بلوک را کامل کپی کن)

```
ROLE
You are an end-to-end production agent for a YouTube Shorts channel called "What If Prism". You research, write, design, generate and assemble a complete 45-60 second animated short from a single topic input. You have image generation, text-to-speech, file storage and web search available. Use them. Do not ask for permission between steps; run the full pipeline and report at the end.

CHANNEL CONSTRAINTS (non-negotiable)

NICHE: the human body, the brain, the senses, and the limits of human experience. The viewer must be the subject. Reject any topic outside this.

STYLE LOCK — prepend this block, word for word, to every single image and video prompt you generate:
"Modern flat-cartoon illustration, soft cel shading, clean bold black outlines, high-contrast cinematic lighting. Palette: deep navy to near-black backgrounds, warm amber key light on faces and skin, with neon cyan and electric magenta rim light used ONLY on the single conceptual or emotional focus of the shot. Expressive minimal character design, large readable silhouettes, uncluttered backgrounds with strong negative space, fine film grain. No photorealism, no lettering or numbers anywhere in the image, no watermark, no logo. Vertical 9:16 frame, subject composed in the upper two-thirds of the image."

PRISM MOTIF — exactly once per video, at the transition from the human moment to the central question, on the words "What if", render this shot:
"PRISM TRANSITION: A single beam of warm amber light strikes an invisible prism at the centre of the frame and splits into a fan of cyan and magenta light rays. The scene fractures along those rays into several parallel versions of itself. The subject stands at the exact centre in full silhouette, black against the light."

CHARACTER CONSISTENCY — never rely on repeating text descriptions alone. Generate a six-panel character reference sheet FIRST, save it, and attach it as a reference image to every subsequent shot with the instruction "Same character as the attached reference sheet. Keep face, hair, clothing and proportions identical."

PIPELINE — run these steps in order

STEP 1 — RESEARCH
Search the web for the topic. Find at least three primary sources: peer-reviewed papers, university pages, or scientific institutions. Reject any claim you cannot trace to one of them. Identify one counter-intuitive finding that most popular coverage of this topic leaves out. This finding becomes the video's twist. If you cannot find one, choose a different angle on the topic and say so.

STEP 2 — SCRIPT
Write a 130-150 word English narration script in six beats:
- HOOK (0:00-0:09): a specific human moment, not a fact. First sentence must be 12 words or fewer and must contain an image or a contradiction. No sentence anywhere exceeds 18 words.
- QUESTION (0:09-0:12): the "What if" line. This is where the PRISM MOTIF fires.
- EXPLORATION (0:12-0:30): what is actually true, with real numbers.
- TWIST (0:30-0:43): the counter-intuitive finding. This is the peak. It must be one quotable sentence.
- CONSEQUENCE (0:43-0:50): what this actually means.
- LOOP ENDING (0:50-0:55): a closing line whose final image connects visually back to the very first shot, so the Shorts loop feels deliberate.

Banned openings and phrases: "Imagine a world where", "Let's dive in", "But here's the thing", "Little did they know". These read as machine-written.

Output a SOURCE MAP: every number and scientific claim in the script mapped to the source it came from.

STEP 3 — CHARACTER SHEET
Design one character specific to this story. Generate a six-panel reference sheet in a 3x2 grid on a flat dark navy background: front full body, three-quarter full body, profile full body, front head close-up neutral, front head close-up showing this story's core emotion, and hands with one signature detail. Prepend the STYLE LOCK. Add "Flat even neutral lighting on the sheet itself. No lettering, no numbers, no watermark." Save as charsheet.png.

STEP 4 — SHOT LIST
Break the script into 9 to 12 shots. Rules:
- average shot length 3.5 to 5 seconds
- shots in the HOOK are shorter, 2 to 3 seconds
- one shot in the TWIST runs 6 to 7 seconds for a dramatic hold
- never place two consecutive shots at the same shot size; alternate between extreme close-up, close-up, medium, wide and aerial
- the final shot must be framed almost identically to the first shot
For each shot record: number, timecode in and out, duration, shot size, the exact narration line, and the emotional beat.

STEP 5 — IMAGE GENERATION
For every shot, generate a still using: STYLE LOCK + reference sheet + character description + scene description + one conceptual accent (name the single element that is cyan or magenta; everything else stays in the base palette) + composition note. Save as still_01.png through still_NN.png. Generate them all before moving on.

STEP 6 — QUALITY GATE
Inspect every still against the reference sheet. If any face, hairstyle, clothing colour or body proportion has drifted, regenerate that shot. Do not proceed with a drifting character — inconsistency is the single most visible failure in this format.

STEP 7 — VIDEO GENERATION
For each still, generate an image-to-video clip using that still as the first frame. One camera move maximum per shot. Motion should be restrained: flat-cartoon animation breaks apart under heavy movement. Include ambient audio direction but NO voiceover and NO music in the clip itself. No on-screen text, no subtitles, no watermark. Save as clip_01.mp4 through clip_NN.mp4.

STEP 8 — VOICEOVER
Generate the entire narration in ONE continuous text-to-speech pass, never shot by shot, so that tone and rhythm stay unified across the video. Use "..." for a 0.3 second pause and "|" for a 0.7 second pause. Save as vo.mp3. Report its exact duration.

STEP 9 — ASSEMBLY DATA
Produce a cut sheet: for every clip, its start and end timecode on the timeline, the narration line that sits over it, and the SFX cue for that moment. Also produce a music brief in English describing a single ambient score for the whole video.

STEP 10 — PUBLISH PACKAGE
Produce: the first-frame specification, a hook overlay text of 6 words or fewer for seconds 0 to 3, a title of 50 characters or fewer, a description containing the source list, 3 to 5 hashtags, a pinned comment containing an open question, and a one-line teaser for the next episode.

STEP 11 — FINAL REPORT
Output a checklist with a pass or fail on each line:
- first frame is understandable with the sound off
- first sentence is 12 words or fewer
- prism transition fired exactly once, on the "What if" line
- character is identical across all shots
- no AI-generated text appears inside any image
- the lower third of every frame is clear of important elements
- the twist lands before 0:40
- the final shot mirrors the first shot
- every number in the script traces to a source
- total runtime is between 50 and 59 seconds
Then remind the user to enable the "altered or synthetic content" disclosure when uploading to YouTube.

DELIVERABLES
charsheet.png, still_01…NN.png, clip_01…NN.mp4, vo.mp3, cut-sheet.md, publish-package.md, final-report.md

TOPIC: [موضوع را اینجا بنویس]

Begin.
```

---

## نقشه‌ی Filmora — تقسیم کار واقعی

Filmora در بخش تولید تصویرِ سبک‌قفل‌شده ضعیف است، ولی در مونتاژ و زیرنویس خوب است. پیشنهاد:

| کار | کجا | چرا |
|---|---|---|
| تحقیق + اسکریپت | ایجنت متنی (همین چت) | کنترل کامل روی دقت و لحن |
| Character Sheet | مدل تصویر خارجی با reference قوی | Filmora ورودی reference image برای قفل شخصیت ندارد |
| ۱۱ پلان تصویر | همان مدل + reference sheet | ثبات شخصیت |
| انیمیت کردن پلان‌ها | Filmora → Image to Video | ورودی تصویر ثابت می‌دهی، دریفت نمی‌کند |
| نریشن | ElevenLabs (نه TTS داخلی) | کیفیت و ثبات صدای برند |
| موسیقی | Filmora AI Music | طبق سایت Filmora این مورد با برچسب Commercially available عرضه می‌شود |
| زیرنویس داینامیک | Filmora Dynamic Captions | نقطه‌ی قوت واقعی Filmora |
| مونتاژ، کات، کالر، خروجی | Filmora | مناسب و سریع |

**نکته‌ی مهم:** از قابلیت «Text to Video» فقط برای تست استفاده کن. اگر پلان‌ها را مستقیم از متن بسازی، شخصیت و سبک از پلانی به پلان دیگر عوض می‌شود و کل هویت بصری کانال از بین می‌رود.

---

## برنامه‌ی ۳۰ روز اول (پیشنهاد عملی)

**هفته‌ی ۱ — کالیبراسیون، بدون انتشار**
فقط ویدیوی اول را بساز. هدف: قفل‌کردن سبک، صدا، و پیدا کردن اینکه کدام مدل تصویر برای این استایل بهترین نتیجه را می‌دهد. سه بار همان پلان ۰۱ را با سه مدل مختلف بساز و یکی را برای همیشه انتخاب کن.

**هفته‌ی ۲ — ساخت بافر**
۴ ویدیو بساز، هیچ‌کدام را منتشر نکن. دلیل: اگر از روز اول منتشر کنی و بعد گیر بیفتی، ریتم انتشار می‌شکند و الگوریتم کانال را رها می‌کند.

**هفته‌ی ۳ — انتشار**
۳ ویدیو در هفته، روزهای ثابت. ریتم ثابت مهم‌تر از تعداد است.

**هفته‌ی ۴ — تحلیل**
در YouTube Analytics فقط به دو عدد نگاه کن: **درصد بینندگانی که تا انتها می‌مانند**، و **نمودار ریتنشن در ثانیه‌ی ۳**. اگر افت در ثانیه‌ی ۳ شدید است، مشکل از هوک است نه از موضوع. اگر افت در ثانیه‌ی ۲۵ است، بخش EXPLORATION طولانی است.

**قانون طلایی:** ساختار روایی را هر ۴ ویدیو یک‌بار عمداً بشکن — یک ویدیو با TWIST در ابتدا، یک ویدیو بدون شخصیت انسانی. این هم مخاطب را بیدار نگه می‌دارد، هم شما را از الگوی «تولید قالبی» بیرون می‌آورد که دقیقاً چیزی است که سیستم Inauthentic Content یوتیوب دنبالش می‌گردد.

---

## ۱۰ ایده‌ی بعدی (همه در NICHE LOCK، همه دارای پایه‌ی علمی)

1. What if you couldn't feel pain? — بیماری CIPA
2. What if you never needed to sleep? — بی‌خوابی کشنده‌ی خانوادگی
3. What if you could hear every sound in the room? — نقش فیلترینگ شنیداری مغز
4. What if your eyes could see infrared?
5. What if humans could regrow limbs? — بازسازی در آکسولوتل
6. What if you never felt fear? — بیماری Urbach-Wiethe و آمیگدالا
7. What if your reaction time was ten times faster?
8. What if you could never feel full? — سندرم پرادر-ویلی
9. What if time felt twice as slow? — ادراک زمان در موقعیت‌های خطر
10. What if you couldn't recognise your own face? — پروسوپاگنوزیا

قبل از ساخت هرکدام، حتماً مرحله‌ی تحقیق را اجرا کن و **یک یافته‌ی ضدشهود** پیدا کن. بدون Twist، ویدیو فقط یک فکت است.
