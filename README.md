# Instructions for WS2812 Arrays

## Ordering from JLCPCB

Visit [JLCPCB.com](https://jlcpcb.com/) or a manufacturer of your choice (Instructions should work almost identically).

Navigate to **Products** → **FR4-PCBs** → **Get Instant Quote**

Upload the needed Gerber-Files as .zip and wait until the upload is completed, now you should see a preview of the uploaded PCBs

### Settings

The first few settings should be set automatically, check these because errors can occur:
- **Base Material:** FR-4
- **Layers:** 2
- **Dimensions:** (should be the numbers of leds per side*10mm e.g. 2 × 2 -→ 20mm × 20mm)
- **PCB Qty:** Enter your needed quantity (*Note:* the more PCBs you order the cheaper they get per Unit)
- **Product Type:** Industrial/Consumer electronics

#### PCB Specifications

- **Different Design:** 1
- **Delivery Format:** Single PCB
- **PCB Thickness:** 1.6mm is preferred to ensure optimal heat dissipation but thinner PCBs can be chosen if you need
- **PCB Color:** White for best optical properties
- **Silkscreen:** (gets chosen automatically)
- **Surface Finish:** HASL(with lead) or LeadFree HASL (LeadFree is recommended for less toxins)

#### High-spec Options

- **Outer Copper Weight:** 1oz
- **Via Covering:** Tented
- **Via Plating Method:** Not Specified
- **Min via hole size/diameter:** 0.3mm/(0.4/0.45mm)
- **Board Outline Tolerance:** ±0.2mm(Regular)
- **Confirm Production file:** No
- **Mark on PCB:** Remove Mark
- **Electrical Test:** Flying Probe Fully Test
- **Gold Fingers:** No
- **Castellated Holes:** No
- **Edge Plating:** No
- **Blind Slots:** No
- **UL Marking:** No

#### Stencil

As there are a lot of components on one PCB a Stencil is recommended, just check **Stencil** at the bottom
- **Framework:** No
- **Step Stencil:** No
- **Nano-Coating:** No
- **Stencil Side:** Top only
- **Dimensions:** Check custom size and give your PCB a border of 10 or 20mm (*Note:* Stencils up to 100mm × 100mm cost the same, keep that in mind when ordering)
- **Stencil Qty:** 1
- **Thickness:** Select by JLCPCB
- **Stencil Process Type:** Solder Paste stencil
- **Polishing Process:** Sanding
- **Fiducials:** No Fiducial
- **Confirm Production file:** Yes (to ensure no errors occurred)
- **Engrave Text:** No
- **Package Box:** With JLCPCB logo

**Done!**
Save the order to your cart and add more PCBs if you like.

*Note:* The Shipping Estimate is not really accurate, depending on weight and delivery time the shipping cost varies a lot.

When added all PCBs just use the checkout like in any other onlineshop.

*Note:* Try different shipping methods and keep in mind that tax and toll might be handled separately with some methods. I recommend *Global Standard Direct Line* or *EuroPacket* for delivery to the EU.

## Assembly

### Needed Equipment and components

- **hot plate or reflow oven** *Note:* An old airfryer also works, just don't use it for food afterwards!
- **solder paste**
- **plastic squeegee or old credit card**
- **fine tweezers**
- **nitrile or latex gloves**
- **tape**
- **X × Y WS2812 LEDs**
- **X × Y 100µF Capacitors** (These are only needed if mentioned in your LEDs Datasheet. If you are not sure, add them as they are beneficial for better data transmission)

### Soldering

#### 1. Build a jig

Build a jig for the PCB you want to build: Use a flat surface, place your PCB and arrange other PCBs around. fix them in place with tape.

![PCB jig](https://github.com/kkitdesign/ws2812-array/blob/40529c479d8c9b486bf6357b3c7a2d97c2f17529/resources/PCB%20jig.jpg)

#### 2. Align stencil

Align your Stencil and fix it on one side with tape

![align stencil](https://github.com/kkitdesign/ws2812-array/blob/40529c479d8c9b486bf6357b3c7a2d97c2f17529/resources/align%20stencil.jpg)

#### 3. Apply solder paste

Put some solder paste on your stencil and spread it evenly over all holes, remove excess paste.

![apply paste](https://github.com/kkitdesign/ws2812-array/blob/40529c479d8c9b486bf6357b3c7a2d97c2f17529/resources/apply%20paste%202.jpg)

#### 4. Remove Stencil and place components

Place your components onto the fresh solder paste. *Note:* Some Components have a distinct orientation, please place accordingly
![place components](https://github.com/kkitdesign/ws2812-array/blob/40529c479d8c9b486bf6357b3c7a2d97c2f17529/resources/place%20components%202.jpg)

#### 5. Heat your reflow device and solder your PCB

Set the correct temperature and place your PCB in/on your reflow device. *Note:* When soldering is finished the PCBs are be hot, please be cautious or burns/injuries may occur!

![reflow](https://github.com/kkitdesign/ws2812-array/blob/40529c479d8c9b486bf6357b3c7a2d97c2f17529/resources/reflow-1.gif)

#### 6. Wire and test

Finally vou can wire your finished PCBs. Use them as you like, but don't exceed the ratings of the PCBs/components!

## Basic examples

If you need some inspiration or a basic script to start with have a look at [scripts](https://github.com/kkitdesign/ws2812-array/tree/main/scripts)!

![example random](https://github.com/kkitdesign/ws2812-array/blob/40529c479d8c9b486bf6357b3c7a2d97c2f17529/resources/random.gif)

## Mounting and integration

The arrays can be combined with fitting diffusers using M3-screws, just make sure they are not too long and damage the front plane. If needed the diffusers can be used to combine multiple arrays, just attach them side by side in your CAD-Software or slicer.

To mount the arrays there are 3mm holes exactly 10mm from the outer edges, the 8×8 and 10×10 also have one mounting hole in the center to prevent the diffuser from bending away. All holes can be used to mount the diffusers to your project, but don't overtighten them and use a nylon washer to prevent scratching the soldermask. In combination with the metal screw shortages could occur.

For mechanical drawings visit [mechanical](https://github.com/kkitdesign/ws2812-array/tree/main/mechanical).


