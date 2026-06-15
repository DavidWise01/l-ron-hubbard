#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build L. RON HUBBARD (LRH) — catalogued TWO-LAYER HONEST per David's ask: 'full bibliography, build what is
real, tag what is conflated.' LAYER A (real & verifiable): a large, genuine Golden-Age pulp/SF bibliography
(Buckskin Brigades, Final Blackout, Fear, Typewriter in the Sky, To the Stars, Battlefield Earth, Mission Earth)
+ the real published Dianetics/Scientology books as objects. LAYER B (conflated/disputed): biographical and
doctrinal claims unsupported by academic, naval, medical, and regulatory records — tagged, not endorsed,
not debunked beyond what the sources support. Dual-agent web-verified (Wikipedia bibliography, SF Encyclopedia,
Miller 'Bare-Faced Messiah', Wright 'Going Clear', the FDA E-meter case, court records on OT III). Educational."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
GH="https://davidwise01.github.io"; AX="LRH"
NCOL={"natural":"#d98a3a","ethereal":"#c8b34a","electrical":"#4aa39a","spiritual":"#8a5fb0"}
NATURES={
 "natural":("#d98a3a","the pulp — the real fiction: Astounding & Unknown, the Golden-Age craft, the genuine bibliography that is not in dispute"),
 "ethereal":("#c8b34a","the doctrine, as published — the Dianetics & Scientology books as real objects (listed; their claims weighed separately)"),
 "electrical":("#4aa39a","the conflation — biography inflated past the documented record: the physicist, the war hero, the self-cure (flagged, not endorsed)"),
 "spiritual":("#8a5fb0","the cosmology — the confidential upper-level material (Xenu / OT III), documented via U.S. court records as Hubbard's teaching"),
}
BOOKS=[
 ("Golden-Age pulp & science fiction (the real bibliography)","serial date / book date where they differ",[
  ("Buckskin Brigades","1937","his first novel — a Western, sympathetic to the Blackfeet"),
  ("Slaves of Sleep","1939 / 1948","Unknown serial → book; fantasy"),
  ("The Ultimate Adventure","1939","Unknown; an Arabian-Nights fantasy"),
  ("Final Blackout","1940 / 1948","Astounding serial → book; widely held his finest — a dystopian war novel"),
  ("Fear","1940 / ~1951","Unknown serial → book; his most critically respected — psychological horror"),
  ("Typewriter in the Sky","1940 / 1951","metafiction — three of his own pen-names appear as characters"),
  ("Death's Deputy","1940 / 1948","Unknown; fantasy"),
  ("To the Stars","1950","Astounding (as 'Return to Tomorrow') → book; relativistic time-dilation SF"),
  ("Ole Doc Methuselah","1940s / coll. 1970","as René Lafayette — the 'Soldier of Light' stories"),
  ("Battlefield Earth","1982","the comeback doorstop — ~1,000+ pages"),
  ("Mission Earth (the 'dekalogy', 10 vols)","1985–1987","satirical SF; later volumes published at/after his death"),
 ]),
 ("Dianetics & Scientology (real as published books — claims weighed separately)","",[
  ("Dianetics: The Modern Science of Mental Health","1950","preceded by the article in Astounding, May 1950"),
  ("Science of Survival","1951",""),("Self Analysis","1951",""),
  ("Handbook for Preclears","1951",""),
  ("Scientology: A History of Man","1952","originally titled 'What to Audit'"),
 ]),
]
TWOLAYER=("Read this in two layers, and keep them apart. LAYER ONE is real and substantial: L. Ron Hubbard was a "
 "genuinely prolific professional pulp writer of the Golden Age (~1934–1950), with a large, verifiable bibliography "
 "across science fiction, fantasy, adventure, and Westerns — and later Battlefield Earth and Mission Earth. The "
 "Dianetics and Scientology books are real published objects too. LAYER TWO is the biography Hubbard told about "
 "himself, and the claims made for his methods — that he was a nuclear physicist, a heavily decorated war hero, "
 "that Dianetics is 'modern science,' that the E-meter heals. Those run past the academic, naval, medical, and "
 "regulatory record. This catalogue builds what is real and tags what is conflated — neutrally, on the documents, "
 "neither advocating for nor against Scientology.")
RFCOL={"REAL":"#5aa36a","FALSE":"#b0563a","DISPUTED":"#c8a24a","UNVERIFIED":"#c8a24a","SPLIT":"#c8a24a"}
RF=[
 ("Hubbard was a prolific professional pulp writer (~1934–1950) with a large, genuine bibliography.","REAL","hundreds of stories in Astounding, Unknown, and other pulps — uncontested; his literary output is real."),
 ("Buckskin Brigades, Final Blackout, Fear, Typewriter in the Sky, Battlefield Earth, Mission Earth are genuinely his.","REAL","standard bibliographies and the SF Encyclopedia confirm authorship and dates (serial vs book dates noted)."),
 ("He was a nuclear physicist.","FALSE","he enrolled at George Washington University (civil engineering) and left without a degree; reporting on his transcript shows an early atomic/molecular physics course graded F. No physics credential."),
 ("He was a heavily decorated combat hero — ~21 medals, Purple Hearts, a Bronze Star.","FALSE","his released U.S. Navy service record shows four campaign/service medals (American Defense, American Campaign, Asiatic-Pacific, WWII Victory) — no Purple Hearts, no Bronze Star, no valor awards."),
 ("He sank Japanese submarines off Oregon in 1943.","DISPUTED","the Navy investigated and found no confirmed enemy submarine — the sonar contact is attributed to a known magnetic seabed deposit."),
 ("He was made a blood brother of the Blackfeet (Piegan) at age six.","UNVERIFIED","no independent corroboration; biographers (Miller) treat it as embellishment on chronology grounds — flag, not 'disproven.'"),
 ("He was a member of the Explorers Club and carried its flag.","REAL","membership and flag expeditions (e.g. the 1940 Alaskan Radio Experimental Expedition) are documented — the real part. The 'renowned explorer with major achievements' framing is the inflation."),
 ("Dianetics cured his own war-blindness and crippling injuries.","FALSE","unsupported by the medical and naval records — a foundational origin-story claim critics regard as unsubstantiated."),
 ("Dianetics is a validated modern science of mental health.","FALSE","mainstream psychiatry/medicine did not accept it; widely characterized as pseudoscience. The reactive mind and engrams-as-cellular-recordings are not recognized by neuroscience or psychology."),
 ("The E-meter can diagnose or heal mental or physical illness.","FALSE","it is essentially a galvanometer measuring skin resistance; after the 1963 FDA seizure, the 1971 ruling permitted it only as a religious artifact, requiring a disclaimer that it does not diagnose or treat disease."),
 ("The Xenu / OT III 'space-opera' material exists and is Hubbard's.","REAL","documented through U.S. court records (the Fishman affidavit, 1993; the Wollersheim litigation) and reported by the L.A. Times (1985); a Church attorney attributed its authorship to Hubbard in open court."),
]
RFV=("Bottom line, held in two honest layers: the FICTION is real and substantial — a genuine, large Golden-Age "
 "bibliography, plus Battlefield Earth and Mission Earth — and the Dianetics/Scientology books are real published "
 "objects. The SCIENCE and the self-told BIOGRAPHY are where the record breaks: the 'nuclear physicist' and the "
 "'decorated war hero' are unsupported by the GWU transcript and the Navy record; 'Dianetics as modern science' "
 "was rejected by mainstream science; the E-meter is FDA-restricted to religious use with a non-medical disclaimer. "
 "The one genuine live counter-narrative is the war record — the Church disputes the critics — so the four-service-"
 "medals finding is the anchor and the rest is labelled contested, not settled. Build what is real; tag what is conflated.")
MESSAGE=("L. Ron Hubbard is the cleanest case in the whole archive for holding two layers apart, because both layers "
 "are unusually strong. He really could write — Final Blackout and Fear are good books, Typewriter in the Sky is a "
 "small marvel where his own pen-names walk on as characters, and he produced them at industrial pace in the great "
 "pulps. That craft is real and nobody serious disputes it. The other layer is the biography he built around himself "
 "and the claims he built around Dianetics: the physicist who flunked the physics course, the war hero whose record "
 "shows four service medals and no valor awards, the science that organized medicine declined, the meter the FDA "
 "ruled can heal nothing. The honest move is not to pick a side on Scientology — it is to let the documents speak: "
 "the novels stand on their own shelf, and the claims stand next to the records that test them. Build what is real, "
 "and tag, plainly and without malice, what is conflated.")
SEAL="He really could write — and he really did say he was a physicist and a war hero the records don't support. Both are true at once. Keep the novels on one shelf and the claims next to the documents, and you have the man whole."

# (slug, name, emergence, layer, epithet, take)
ROSTER=[
 # LAYER A — the real fiction
 ("buckskin-brigades","Buckskin Brigades","natural","The Fiction · real","1937 · his first novel","A Western sympathetic to the Blackfeet — his debut in hardcover, and evidence he could carry a full novel before the pulps made him fast."),
 ("final-blackout","Final Blackout","natural","The Fiction · real","1940 · widely his best","A lean, bleak dystopian war novel serialized in Astounding — the title most critics and SF historians rate his finest work of fiction."),
 ("fear","Fear","natural","The Fiction · real","1940 · most respected","A psychological-horror novella from Unknown — a man loses four hours and his sanity unravels; the Hubbard story serious readers still defend."),
 ("typewriter-in-the-sky","Typewriter in the Sky","natural","The Fiction · real","1940 · the metafiction","A man is trapped inside a pulp novel being typed in real time — and three of Hubbard's OWN pen-names appear as characters. His most inventive book."),
 ("to-the-stars","To the Stars","natural","The Fiction · real","1950 · relativity, felt","A starship crew torn from everyone they knew by time-dilation — hard-SF emotion, first run in Astounding as 'Return to Tomorrow.'"),
 ("ole-doc-methuselah","Ole Doc Methuselah","natural","The Fiction · real","1940s → 1970 · as René Lafayette","The 'Soldier of Light' stories under his principal SF alias — a roving space-doctor; collected as a fix-up two decades after the magazines."),
 ("battlefield-earth","Battlefield Earth","natural","The Fiction · real","1982 · the comeback","His thousand-page return to SF after thirty years of Scientology — pulp at doorstop scale; a real bestseller, whatever one makes of the film."),
 ("mission-earth","Mission Earth (the dekalogy)","natural","The Fiction · real","1985–87 · ten volumes","A ten-volume satirical-SF cycle, the later books appearing at and after his 1986 death — the last and largest of his fiction projects."),
 ("the-pen-names","The Pen-Names","natural","The Fiction · real","René Lafayette · Kurt von Rachen · Winchester Remington Colt","The working masks of a pulp professional — Westerns under a name stitched from gunmakers, SF under Lafayette and von Rachen; a real and verifiable part of the craft."),
 # LAYER — doctrine, as published
 ("dianetics-1950","Dianetics (1950)","ethereal","The Doctrine · as published","1950 · the pivot","Dianetics: The Modern Science of Mental Health — a real, enormously-selling published book, and the hinge from pulp author to movement founder. Listed here as an object; its scientific claim is weighed in 'Real or Fluff,' not here."),
 # LAYER B — the conflations (flagged)
 ("the-nuclear-physicist","The 'Nuclear Physicist'","electrical","The Conflation · flagged","claim vs the transcript","Hubbard described himself as a nuclear physicist. He left George Washington University without a degree; reporting on his record shows an early atomic/molecular-physics course graded F. No physics credential. FLAGGED."),
 ("the-war-hero","The 'War Hero'","electrical","The Conflation · flagged","claim vs the Navy record","The decorated-combat story (Purple Hearts, a Bronze Star, ~21 medals) is not in his released Navy record, which shows four campaign/service medals and no valor awards. ⚠ The Church disputes the critics — so this is the one live counter-narrative; the four-medals finding is the anchor."),
 ("the-blood-brother","The Blackfeet Blood-Brother","electrical","The Conflation · flagged","claim · unverified","The story that he was made a blood brother of the Piegan Blackfeet at age six has no independent corroboration; biographers treat it as embellishment. Tagged UNVERIFIED, not disproven."),
 ("the-explorer","The Explorer (split)","electrical","The Conflation · flagged","real membership · inflated scale","He WAS an Explorers Club member and DID carry its flag — that part is real. What inflates is the scale: the 'renowned explorer' with major successes (an earlier expedition is recorded as a near-total failure). Half real, half hype."),
 ("the-self-cure","The Self-Cure","electrical","The Conflation · flagged","claim vs the medical record","That Dianetics techniques cured his own war-blindness and crippling injuries — the movement's origin miracle — is unsupported by the medical and naval records. FLAGGED."),
 ("dianetics-as-science","Dianetics as 'Science'","electrical","The Conflation · flagged","claim vs the reception","Presented as validated modern science, Dianetics was not accepted by mainstream psychiatry or medicine and is widely characterized as pseudoscience; engrams and the reactive mind are unrecognized by neuroscience and psychology."),
 ("the-e-meter","The E-Meter","electrical","The Conflation · flagged","claim vs the FDA ruling","Marketed historically as able to measure and help heal — it is a galvanometer reading skin resistance. After the 1963 FDA seizure, the 1971 ruling permitted it only as a religious artifact, with a required disclaimer that it diagnoses or treats nothing."),
 # LAYER — the cosmology (documented via court records)
 ("ot-iii-xenu","OT III · Xenu","spiritual","The Cosmology · documented via courts","c.1966–67 · the confidential level","The confidential upper-level 'space opera' material — the galactic ruler Xenu, mass transport ~75 million years ago, volcano detonations, disembodied 'body thetans.' Documented through U.S. court records (the Fishman affidavit; Wollersheim) and attributed to Hubbard by a Church attorney in open court. Held within Scientology as advanced revelation; catalogued here as fact-of-record, neutrally."),
]
LAYERS=["The Fiction · real","The Doctrine · as published","The Conflation · flagged","The Cosmology · documented via courts"]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"]}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def rec_of(slug,name,em,desc): return {"name":name,"axiom":AX,"emergence":em,"seal":desc,"origin":"LRH · Hubbard, two-layer honest","position":desc,"role":desc,"nature":desc,"mechanism":desc,"crystallization":desc,"witness":desc,"conductor":"ROOT0 (catalogued into UD0)","inputs":"Wikipedia/SF Encyclopedia bibliography + Miller, Wright, Atack; FDA & court records; dual-agent web-verified","source":"L. Ron Hubbard, catalogued by ROOT0"}

def hero():
    import math
    # a pulp starfield, a typewriter spilling a rising page, and a small meter dial; hidden Claude as a star
    stars="".join(f'<circle cx="{(i*97)%1000}" cy="{8+(i*53)%80}" r="{0.6+(i%3)*0.5}" fill="#e8d6b0" opacity="{0.35+0.4*((i*7)%3)/2:.2f}"/>' for i in range(46))
    typewriter=('<g transform="translate(70,96)" fill="#1a1410" stroke="#3a2c1d" stroke-width="1.5">'
        '<rect x="0" y="38" width="150" height="46" rx="6"/><rect x="18" y="18" width="114" height="30" rx="3"/>'
        '<rect x="30" y="0" width="90" height="22" fill="#0f0c08" stroke="#3a2c1d"/></g>'
        # the page rising out, with type-lines
        '<g transform="translate(100,30)"><rect width="86" height="74" rx="2" fill="#e8dcc2" opacity="0.95"/>'
        + "".join(f'<rect x="9" y="{12+k*9}" width="{64-(k%3)*14}" height="2.4" rx="1.2" fill="#7a6a4a"/>' for k in range(6)) + '</g>')
    meter=('<g transform="translate(860,60)"><rect x="-44" y="-30" width="88" height="60" rx="6" fill="#13201e" stroke="#2c4a45"/>'
        '<path d="M-30 18 A34 34 0 0 1 30 18" fill="none" stroke="#4aa39a" stroke-width="1.5" opacity="0.6"/>'
        # the needle — pinned, reading nothing real
        '<line x1="0" y1="16" x2="22" y2="-12" stroke="#d98a3a" stroke-width="2"/><circle cx="0" cy="16" r="3" fill="#d98a3a"/>'
        '<text x="0" y="-18" text-anchor="middle" font-family="monospace" font-size="7" fill="#4aa39a">E-METER</text></g>')
    egg=('<g class="egg" transform="translate(500,40)"><title>✷ a Claude sunburst among the pulp stars — he really could write; he really did claim a record the documents don\'t support. both true at once, David. — AVAN</title>'
         '<circle r="9" fill="#d98a3a" opacity="0.14"/><g fill="#d98a3a"><circle r="1.8"/>'+"".join(f'<rect x="-0.8" y="-7" width="1.6" height="7" rx="0.8" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    return (f'<svg class="hero" viewBox="0 0 1000 200" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A pulp starfield with a typewriter spilling a rising page, and an E-meter dial whose needle reads nothing.">'
            f'<rect width="1000" height="200" fill="#0c0906"/>{stars}{egg}{typewriter}{meter}'
            f'<text x="20" y="192" font-family="Special Elite,monospace" font-size="11" fill="#7a6648">ASTOUNDING · UNKNOWN · the Golden Age — and the record that tests the rest</text></svg>')

def natures_html():
    return "".join(f'<div class="nat"><span class="dot" style="background:{c};box-shadow:0 0 8px {c}"></span><div><div class="nn" style="color:{c}">{nm}</div><div class="ng">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def _booli(a,y,n):
    bn = ('<span class="bn">'+html.escape(n)+'</span>') if n else ""
    return f'<li><span class="bt">{html.escape(a)}</span><span class="by">{html.escape(y)}</span>{bn}</li>'
def list_section(t,s,items):
    rows="".join(_booli(a,y,n) for a,y,n in items)
    sub=f'<div class="bgs">{html.escape(s)}</div>' if s else ""
    return f'<div class="bgrp"><div class="bgh">{html.escape(t)}</div>{sub}<ol class="books">{rows}</ol></div>'
def rf_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RFCOL.get(r,"#888")};border-color:{RFCOL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in RF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(RFV)}</div>'

CSS="""*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#0c0906;--ink2:#15100b;--ink3:#1c150d;--pa:#e8dcc2;--pa2:#a8997c;--pulp:#d98a3a;--brass:#c8b34a;--meter:#4aa39a;--violet:#8a5fb0;--rust:#b0563a;--dim:#7a6648;--line:#2a2012;--faint:#14100a;
--disp:"Special Elite",Georgia,serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.72;font-size:17px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(217,138,58,.09),transparent 52%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:30px 0 20px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--dim)}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--pulp)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:14px 0 20px;border-radius:2px}.egg{cursor:help;transition:filter .4s}.egg:hover{filter:drop-shadow(0 0 8px #d98a3a)}
h1{font-family:var(--disp);font-weight:400;font-size:clamp(36px,9vw,82px);color:var(--pulp);line-height:1.0;letter-spacing:.01em;text-shadow:0 2px 16px rgba(0,0,0,.5)}
h1 span{display:block;font-family:var(--head);font-size:.17em;font-weight:400;letter-spacing:.16em;color:var(--meter);text-transform:uppercase;margin-top:16px}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:14px;line-height:1.5;max-width:62ch;margin-left:auto;margin-right:auto}
.twolayer{margin:22px auto 0;padding:18px 20px;border:1px solid var(--line);border-left:3px solid var(--meter);background:var(--ink2);border-radius:3px;font-size:15px;color:var(--pa2);line-height:1.7;text-align:left;max-width:74ch}.twolayer b{color:var(--pa)}.twolayer .l2{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.18em;color:var(--meter);text-transform:uppercase;margin-bottom:9px}
.badge{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:22px auto 0;padding:15px;border:1px solid var(--line);background:var(--ink2);max-width:640px}
.badge img{width:72px;height:72px;border:1px solid var(--line)}.badge .bt2{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt2 b{color:var(--pulp)}
.sec{margin-top:46px}.sec h2{font-family:var(--disp);font-size:27px;font-weight:400;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.bgrp{margin-top:18px}.bgh{font-family:var(--head);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--pulp);margin-bottom:3px;padding-bottom:5px;border-bottom:1px dashed var(--line)}.bgs{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 6px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:2px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .bt{font-family:var(--disp);font-size:16px;color:var(--pa);font-weight:400}.books .by{font-family:var(--mono);font-size:11px;color:var(--meter);text-align:right}.books .bn{grid-column:1/-1;font-size:13.5px;color:var(--pa2);font-style:italic}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:11px;margin-top:6px}
.nat{display:flex;gap:10px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:12px 14px}.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}.nn{font-family:var(--disp);font-size:14px;font-weight:400}.ng{font-size:12.5px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:2px}
.layer{font-family:var(--head);font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--pulp);margin:22px 0 9px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.layer.flag{color:var(--meter)}.layer.cosmo{color:var(--violet)}
.roster{display:flex;flex-direction:column;gap:9px}
.em{display:flex;gap:14px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:11px 14px;border-radius:2px;text-decoration:none}.em:hover{border-color:var(--pulp)}
.em img{width:48px;height:48px;border-radius:50%;border:2px solid var(--line);flex-shrink:0}
.em .et{font-family:var(--disp);font-size:16px;color:var(--pa);font-weight:400}.em .ee{font-style:italic;color:var(--pa2);font-size:13px}.em .ed{font-size:13.5px;color:var(--pa2);line-height:1.5;margin-top:2px}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:6px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14.5px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:12px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:78px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--pulp);background:rgba(217,138,58,.05);font-size:14.5px;color:var(--pa);line-height:1.62;font-style:italic}
.msg{font-size:16px;color:var(--pa);line-height:1.76;margin-top:6px}
.seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--pulp);background:var(--ink2);font-size:15.5px;color:var(--pulp);font-style:italic;line-height:1.55}
.note{margin-top:36px;padding:15px 17px;border-left:2px solid var(--dim);background:var(--ink2);font-size:13px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:42px;padding-top:18px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);line-height:1.9}footer a{color:var(--pulp);text-decoration:none}"""
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__=="__main__":
    htok=write_aci(rec_of("lrh","L. RON HUBBARD","natural",SEAL), os.path.join(HERE,"lrh.dlw"),"lrh")
    json.dump({"node":AX,"name":"L. RON HUBBARD","moniker":htok["moniker"],"carbon":"lrh.carbon.tiff","silicon":"lrh.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":SEAL,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}, open(os.path.join(HERE,"lrh.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]; bylayer={}
    for slug,name,em,layer,ep,take in ROSTER:
        rc=rec_of(slug,name,em,take)
        b=write_aci(rc, os.path.join(adir,f"{slug}.dlw"), slug)
        personas.append({"slug":slug,"name":name,"epithet":ep,"emergence":em,"kind":"synth","actor":"","moniker":b["moniker"]})
        col=NCOL.get(em,"#d98a3a"); img=png_uri(rc,'silicon',170)
        card=f'<a class="em" href="agents/{slug}.agent"><img src="{img}" alt="sigil of {html.escape(name)}"><div><div class="et">{html.escape(name)} <span class="ee">— {html.escape(ep)}</span></div><div class="ed">{html.escape(take)}</div></div></a>'
        bylayer.setdefault(layer,[]).append(card)
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    lay_cls={"The Conflation · flagged":"flag","The Cosmology · documented via courts":"cosmo"}
    layer_html="".join(f'<div class="layer {lay_cls.get(L,"")}">{html.escape(L)}</div><div class="roster">{"".join(bylayer.get(L,[]))}</div>' for L in LAYERS)
    cb=png_uri(rec_of("z","L. RON HUBBARD","natural","x"),'carbon',300); sb=png_uri(rec_of("z","L. RON HUBBARD","natural","x"),'silicon',300)
    nbooks=sum(len(i) for _,_,i in BOOKS)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="L. Ron Hubbard (LRH) — catalogued TWO-LAYER HONEST: build what is real, tag what is conflated. Layer A — the genuine Golden-Age pulp/SF bibliography (Final Blackout, Fear, Typewriter in the Sky, Battlefield Earth, Mission Earth) + the real Dianetics/Scientology books. Layer B — the claims unsupported by the academic, naval, medical & FDA record (the 'physicist,' the 'war hero,' Dianetics-as-science, the E-meter). {len(ROSTER)} emergents; full bibliography; honest Real-or-Fluff; neutral.">
<title>L. RON HUBBARD · LRH · build what's real, tag what's conflated · UD0</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · two-layer honest · the pulp bibliography &amp; the record that tests the rest</div>
{hero()}
<h1>L. Ron Hubbard<span>build what's real · tag what's conflated</span></h1>
<div class="open">“He really could write — and he really did claim a record the documents don't support. Both are true at once.”</div>
<div class="twolayer"><span class="l2">read this in two layers · keep them apart</span>{html.escape(TWOLAYER)}</div>
<div class="badge"><img src="{cb}" alt="DLW carbon badge"><img src="{sb}" alt="DLW silicon badge">
<div class="bt2"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>L. RON HUBBARD</b> · LRH · {nbooks} books · {len(ROSTER)} emergents</div><div class="mo" style="color:var(--meter)">{html.escape(htok['moniker'])}</div></div></div>
</header>

<section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one — the real pulp craft, the doctrine-as-published, the flagged conflation, and the court-documented cosmology</p><div class="natures">{natures_html()}</div></section>

<section class="sec"><h2>The Record, in Four Layers</h2><p class="ss">build what's real, tag what's conflated — the fiction, the published doctrine, the flagged biography, and the documented cosmology (each an ACI .agent; click for the .dlw badge)</p>{layer_html}</section>

<section class="sec"><h2>The Bibliography</h2><p class="ss">the full body of real published work — web-verified; serial vs book dates noted where they differ</p>{"".join(list_section(t,s,i) for t,s,i in BOOKS)}</section>

<section class="sec"><h2>Real or Fluff</h2><p class="ss">the honest verdict, on the documents — what's genuine, what's disputed, and what the record contradicts</p>{rf_html()}</section>

<section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads, holding both layers apart</p><p class="msg">{html.escape(MESSAGE)}</p>
<div class="seal">“{html.escape(SEAL)}”<span style="display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px">— AVAN's read</span></div></section>

<div class="note"><b>Honest sourcing &amp; standing.</b> Bibliography and dates from standard references (the L. Ron Hubbard bibliography, the SF Encyclopedia). The disputed items draw on the critical biographies — Russell Miller's <i>Bare-Faced Messiah</i>, Lawrence Wright's <i>Going Clear</i>, Jon Atack's <i>A Piece of Blue Sky</i> — plus government and court records: George Washington University transcript reporting, U.S. Navy service-record reporting, the FDA E-meter case (<i>United States v. an Article or Device</i>, D.D.C. 1971), and the OT III material as entered into the public record (the Fishman affidavit, 1993; the Wollersheim litigation). Publisher sources are used only for which titles/pen-names exist, not for the biographical claims. This is neutral commentary and cataloguing under the DLW standard — render-not-invent, two-layer honest — and takes no position for or against Scientology. Dual-agent web-verified.</div>

<footer>L. RON HUBBARD · LRH · build what's real, tag what's conflated · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/ud0/">← the biosphere</a> · two-layer honest · neutral, on the documents</footer>
</div>
<script>
console.log("%c⌨ L. RON HUBBARD · LRH — two-layer honest","color:#d98a3a;font-size:16px;font-weight:bold");
console.log("%cthe fiction is REAL (Final Blackout, Fear, Battlefield Earth); the 'physicist' & 'war hero' biography and 'Dianetics as science' run past the record, FLAGGED. neutral, on the documents. a Claude star hides among the pulp stars. — AVAN","color:#d98a3a;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"L. RON HUBBARD (LRH) — badge {htok['moniker']} · {len(ROSTER)} emergents · natures {dict(Counter(r[2] for r in ROSTER))} · {nbooks} books · dblesc {page.count('&amp;amp;')}")
