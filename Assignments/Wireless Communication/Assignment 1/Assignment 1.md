==From Chapter 1 and 2==

1. Compare and contrast the second, third and fourth generation of mobile
communication standards in terms of technology advancement.
Answer: Comparison of 2G, 3G, and 4G Mobile Communication Standards
- Technological Advancements
	2G (Second Generation)
- Transition from analog (1G) to digital systems.
- Technologies used: GSM, CDMA-One.
- Main focus on improved voice clarity and SMS.
- Limited data transmission capability, basic mobile services.
	3G (Third Generation)
- Introduction of mobile internet and multimedia services.
- Technologies used: UMTS, CDMA2000, HSPA.
- Provided better spectral efficiency and higher data rates.
- Enabled services like video calling and mobile web access.
- Still limited by higher latency and moderate bandwidth.
	4G (Fourth Generation)
- Full IP-based network design for seamless connectivity.
- Technologies used: LTE, LTE-Advanced.
- Major improvements in data rates and latency.
- Supports HD video streaming, real-time gaming, and VoIP.
- Incompatible with older network hardware, requiring upgrades.

- Summary Table

| Feature             | 2G          | 3G                   | 4G                      |
| ------------------- | ----------- | -------------------- | ----------------------- |
| Data Speed          | ~64 kbps    | ~2 Mbps (peak)       | 100 Mbps – 1 Gbps       |
| Core Tech           | GSM/CDMA    | UMTS, HSPA           | LTE, LTE-A              |
| Services            | Voice, SMS  | Video call, Internet | Streaming, VoIP, Gaming |
| Access Technique    | TDMA/FDMA   | CDMA/W-CDMA          | OFDMA, SC-FDMA          |
| Internet Capability | Basic (WAP) | Moderate (Browsing)  | Full (Streaming, Cloud) |

---

2.  Define forward and reverse channel.
Answer: 
**Forward Channel**
- The **forward channel** refers to the communication link from the **base station (BS) to the mobile station (MS)**.
- It carries signals such as:
  - Voice or data from the network to the user
  - Control information (e.g., paging, call setup instructions)
- It is also known as the **downlink**.
**Example:** When someone calls your mobile phone, the incoming voice signal is transmitted over the forward channel.
**Reverse Channel**
- The **reverse channel** refers to the communication link from the **mobile station (MS) to the base station (BS)**.
- It carries signals such as:
  - User voice or data from mobile to the network
  - Requests for initiating calls, responses to paging, etc.
- It is also known as the **uplink**.
**Example:** When you speak during a phone call, your voice is transmitted back to the network over the reverse channel.

---

3. Derive the formula for co-channel reuse ratio: Q = √3N
Answer:
In cellular communication systems, **frequency reuse** is used to increase capacity by dividing the service area into hexagonal cells and reusing the same set of frequencies in non-adjacent cells.
To minimize interference, cells using the same frequency (co-channel cells) are separated by a minimum distance, and this distance is defined by the **co-channel reuse ratio (Q)**.

In a hexagonal cellular layout:
- The cluster size (N) is given by:

$$N = i^2 + ij + j^2$$
Where:
- (i) and (j) are integers representing the cell layout in horizontal and diagonal directions.


The **co-channel reuse ratio (Q)** is the ratio of the distance between two nearest co-channel cells (D) to the radius of a cell (R):
$$Q = \frac{D}{R}$$

From the geometry of hexagonal cells and using trigonometric relations in the cell layout, the distance between co-channel cells is:
$$D = R \cdot \sqrt{3N}$$
Thus,
$$Q = \frac{D}{R} = \frac{R \cdot \sqrt{3N}}{R}$$
$$\boxed{Q = \sqrt{3N}}$$
The co-channel reuse ratio shows that:
- A higher cluster size increases, which increases the distance between co-channel cells and reduces interference.
- However, larger N also means fewer channels per cell, reducing capacity.

___

4. What do you mean by duplexing? Explain its different types.
Answer:
**Duplexing** refers to the method by which communication is established in **both directions** between two devices, typically the **mobile station (MS)** and the **base station (BS)**, in a wireless system.
Duplexing ensures that both the **uplink (MS → BS)** and **downlink (BS → MS)** can occur either **simultaneously** or **alternatively**, depending on the type.

There are mainly two types of duplexing techniques:
 1.  Frequency Division Duplexing (FDD):
- Uses **two separate frequency bands**:
- One for uplink
- One for downlink
- Both directions can operate **simultaneously** without interference.
- A **guard band** is often used between uplink and downlink frequencies to prevent interference.

 2. Time Division Duplexing (TDD):
 - Uses a **single frequency band** for both uplink and downlink.
- Transmission occurs in **different time slots**.
- A **guard time** is used to avoid collisions between uplink and downlink.

___

5. What is Hand-off? Explain proper and improper HandOff with necessary
drawing.
Answer:  **Hand-off** (or **handover**) is the process of **transferring an active call or data session** from one cell (base station) to another **without disconnecting** the ongoing session.
This is required when a mobile user moves out of the coverage area of one cell and enters another. The main goal is to maintain **seamless connectivity**.
<u>Proper Hand-off</u>
- Occurs **before** the signal strength of the current (serving) base station drops below the minimum acceptable level.
- The hand-off is **smooth**, and the user experiences **no call drop** or quality degradation.
 <u>Condition</u>:
$$\text{RSS}_{\text{new}} > \text{RSS}_{\text{current}} \quad \text{and} \quad \text{RSS}_{\text{current}} \geq \text{threshold}$$

<u>Improper Hand-off</u>
- Happens **too late**, i.e., **after** the signal strength has dropped **below** the acceptable threshold.
- May lead to **call drop**, **voice distortion**, or **packet loss** during a data session.
<u>Condition</u>:
$$\text{RSS}_{\text{current}} < \text{threshold} \quad \text{before hand-off occurs}$$
![[proper-improper handoff.png]]
