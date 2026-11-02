import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Oakhaven AI Village — Emotional Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_source = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Oakhaven AI Village — Research Platform</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
:root {
    --bg: #09121c; --panel: #111e2b; --panel2: #162737; --line: #273b4d; 
    --text: #e8f1f7; --muted: #8da4b6; --mint: #63e6be; --blue: #69b7ff; 
    --gold: #ffc86a; --red: #ff6b6b; --radius: 14px;
}
* { box-sizing: border-box; }
body { 
    margin: 0; 
    background: var(--bg); 
    color: var(--text); 
    font: 14px/1.45 Inter, Segoe UI, Arial, sans-serif; 
    min-height: 100vh; 
    overflow-x: hidden;
}
button { font: inherit; cursor: pointer; transition: .18s; }
button:hover { filter: brightness(1.12); transform: translateY(-1px); }

/* Fully Responsive App Grid */
.app { 
    min-height: 100vh; 
    display: grid; 
    grid-template-columns: 220px minmax(0, 1fr) 280px; 
}

/* Sidebar Styling */
.sidebar { background: #0b141f; border-right: 1px solid var(--line); padding: 20px 14px; display: flex; flex-direction: column; gap: 20px; }
.brand { display: flex; align-items: center; gap: 10px; padding: 0 6px; }
.logo { height: 40px; width: 40px; display: grid; place-items: center; border-radius: 12px; background: linear-gradient(135deg, var(--mint), var(--blue)); color: #08251e; font-size: 22px; font-weight: 900; }
.brand strong { font-size: 14px; letter-spacing: .5px; }
.brand small { display: block; color: var(--muted); font-size: 10px; }

.navlabel { padding: 0 10px; color: #647d90; font-size: 10px; letter-spacing: 1.6px; text-transform: uppercase; }
.nav { display: grid; gap: 4px; margin-top: 5px; }
.nav a { padding: 10px 11px; color: #a8bbc9; text-decoration: none; border: 1px solid transparent; border-radius: 10px; display: flex; gap: 10px; align-items: center; font-size: 13px;}
.nav a.active { background: #17352f; border-color: #285548; color: var(--mint); }
.sidebox { margin-top: auto; padding: 14px; background: var(--panel); border: 1px solid var(--line); border-radius: 12px; color: var(--muted); font-size: 11px; }
.dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--mint); box-shadow: 0 0 10px #63e6be; margin-right: 7px; }

main { padding: 20px; min-width: 0; }
.topbar { display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; }
.eyebrow { color: var(--mint); font-size: 10px; font-weight: 800; letter-spacing: 1.8px; text-transform: uppercase; }
.topbar h1 { font-size: clamp(20px, 3vw, 26px); margin: 4px 0; }
.subtitle { color: var(--muted); font-size: 12px; line-height: 1.4; }
.controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.clockbox { border: 1px solid var(--line); background: #0c1722; border-radius: 10px; padding: 8px 12px; color: var(--muted); font-size: 11px; display: flex; align-items: center; gap: 6px;}
.speed-group { display: flex; background: #0c1722; border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
.speed-btn { border: 0; border-radius: 0; padding: 8px 12px; background: transparent; color: var(--muted); font-size: 12px; }
.speed-btn.active { background: #2469a6; color: #fff; }
.toggle { border: 1px solid #397ec0; background: #2776bb; color: white; border-radius: 10px; padding: 8px 14px; font-weight: 700; font-size: 12px; }

.metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 15px; }
.metric, .panel { background: linear-gradient(145deg, #132231, #101a26); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: 0 8px 24px #0002; min-width: 0; }
.metric { padding: 14px; }
.metrichead { display: flex; justify-content: space-between; color: var(--muted); font-size: 11px; }
.metricvalue { font-size: 24px; font-weight: 800; letter-spacing: -.5px; margin: 5px 0 2px; font-variant-numeric: tabular-nums; }
.metricfoot { font-size: 10px; color: var(--muted); }
.green { color: var(--mint); }
.yellow { color: var(--gold); }

.layout { display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(320px, 1fr); gap: 15px; }
.panel { padding: 16px; }
.panelhead { display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; margin-bottom: 12px; flex-wrap: wrap;}
.panelhead h2 { font-size: 14px; margin: 0; font-weight: 600;}
.panelhead p { font-size: 10px; color: var(--muted); margin: 3px 0 0; }
.pill { border-radius: 20px; background: #183b32; color: var(--mint); font-size: 10px; padding: 4px 8px; white-space: nowrap; font-weight: 600; margin-top: 2px;}

#canvas-container { position: relative; width: 100%; aspect-ratio: 16/10; min-height: 250px; border: 1px solid #294252; border-radius: 12px; overflow: hidden; background: #13252f; box-shadow: inset 0 0 40px rgba(0,0,0,0.5); }
.map-svg { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; }
#simCanvas { display: block; width: 100%; height: 100%; position: relative; z-index: 1; background: transparent; }
.rain-overlay { position: absolute; inset: 0; z-index: 2; background-image: repeating-linear-gradient(105deg, transparent 0 18px, #ffffff16 19px 20px, transparent 21px 36px); pointer-events: none; opacity: 0; transition: opacity .6s; animation: rainFall .5s linear infinite; }
.raining .rain-overlay { opacity: .6; }
@keyframes rainFall { to { background-position: -20px 100px; } }

.agent-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 10px; margin-top: 12px; max-height: 480px; overflow-y: auto; padding-right: 4px;}
.agent-grid::-webkit-scrollbar { width: 4px; }
.agent-grid::-webkit-scrollbar-thumb { background: #374755; border-radius: 4px; }

.agent-card { background: #152433; border: 1px solid #263b4d; border-radius: 10px; padding: 10px; display: flex; flex-direction: column; gap: 6px; position: relative;}
.mood-bar { height: 3px; width: 100%; background: #0c1722; border-radius: 2px; overflow: hidden; margin-top: 2px;}
.mood-fill { height: 100%; border-radius: 2px; transition: width 0.3s, background 0.3s; }
.needs-bars { display: flex; flex-direction: column; gap: 3px; }
.need-row { display: flex; align-items: center; gap: 5px; font-size: 9px; color: var(--muted); }
.need-track { flex: 1; height: 4px; background: #0c1722; border-radius: 2px; overflow: hidden; }
.need-fill { height: 100%; border-radius: 2px; transition: width 0.3s; }
.need-fill.critical { background: var(--red) !important; }
.inv-bar { display: flex; justify-content: space-between; font-size: 10px; background: #0b141f; padding: 4px 6px; border-radius: 6px; border: 1px solid #1e3040;}

.logpanel { display: flex; flex-direction: column; height: 100%; max-height: 700px;}
.logtop { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding-bottom: 13px; border-bottom: 1px solid var(--line); }
.log-container { font-family: Consolas, Monaco, monospace; scrollbar-width: thin; scrollbar-color: #475569 #1e293b; flex: 1; overflow-y: auto; padding-top: 10px; display: flex; flex-direction: column; gap: 8px;}
.log-container::-webkit-scrollbar { width: 6px; }
.log-container::-webkit-scrollbar-thumb { background: #475569; border-radius: 6px; }
.log-entry { border-radius: 8px; padding: 10px; font-size: 11px; line-height: 1.5; border: 1px solid #2a4051; }
.log-entry.system2 { border-color: rgba(244, 114, 182, 0.4); background: rgba(80, 20, 40, 0.2); }
.log-entry.system1 { background: rgba(30, 41, 59, 0.4); }
.log-entry.economy { border-color: rgba(255, 200, 106, 0.4); background: rgba(133, 77, 14, 0.15); }

.right-sidebar { background: #09121c; border-left: 1px solid var(--line); padding: 20px; display: flex; flex-direction: column; gap: 20px; }
.control-label { font-size: 11px; color: var(--muted); margin-bottom: 6px; display: block; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;}
.control-select { width: 100%; padding: 10px; background: #132231; border: 1px solid var(--line); color: var(--text); border-radius: 8px; outline: none; font-size: 12px; cursor: pointer; transition: 0.2s;}
.control-select:focus { border-color: var(--mint); }
.control-btn { width: 100%; padding: 10px; background: #1f2937; border: 1px solid var(--line); color: white; border-radius: 8px; font-size: 12px; font-weight: 600; text-align: center; }
.control-btn.danger { background: #451a1a; border-color: #7f1d1d; color: #fca5a5; }

/* Device Responsiveness */
@media(max-width:1200px){
    .layout { grid-template-columns: 1fr; }
    .logpanel { max-height: 400px; }
}
@media(max-width:900px){
    .app { grid-template-columns: 1fr; display: flex; flex-direction: column;}
    .sidebar { border-right: none; border-bottom: 1px solid var(--line); flex-direction: row; flex-wrap: wrap; align-items: center; padding: 12px; gap: 12px;}
    .navlabel, .sidebox { display: none; }
    .nav { display: flex; overflow: auto; margin: 0; width: 100%;}
    .nav a { white-space: nowrap; padding: 8px 10px; }
    .nav a:not(.active) { display: none; }
    .right-sidebar { border-left: none; border-top: 1px solid var(--line); flex-direction: row; flex-wrap: wrap; }
    .right-sidebar > div { flex: 1; min-width: 200px; }
    .agent-grid { grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); }
}
@media(max-width:600px){
    main { padding: 12px; }
    .topbar { align-items: flex-start; flex-direction: column; gap: 12px;}
    .controls { width: 100%; display: grid; grid-template-columns: 1fr 1fr; }
    .speed-group { grid-column: span 2; display: flex; }
    .speed-btn { flex: 1; }
    .toggle { grid-column: span 2; }
    .metrics { grid-template-columns: 1fr 1fr; gap: 8px; }
    .metric { padding: 10px; }
    .metricvalue { font-size: 20px; }
    .right-sidebar { flex-direction: column; }
    #canvas-container { min-height: 200px; }
}
</style>
</head>
<body>
<div class="app">
<aside class="sidebar">
  <div class="brand"><div class="logo">⌂</div><div><strong>OAKHAVEN AI</strong><small>Village research simulator</small></div></div>
  <div style="flex:1"><nav class="nav">
    <a class="active" href="#overview">◫ Environment Dashboard</a>
  </nav></div>
  <div class="sidebox">
    <div style="font-weight:700;color:var(--text);margin-bottom:7px"><span class="dot"></span>Engine v3.0</div>
    Emotional Baseline Architecture<br><br>
    <span style="color:var(--mint)">Health</span> · Needs & Energy<br>
    <span style="color:var(--blue)">Social</span> · Crowd Proximity<br>
    <span style="color:var(--gold)">Economy</span> · Wealth & Trade
  </div>
</aside>

<main id="overview">
<header class="topbar">
  <div>
    <div class="eyebrow">Research environment / Oakhaven</div>
    <h1>Holistic Emotion Simulation</h1>
    <div class="subtitle">Agents dynamically evaluate happiness based on economic wealth, physical health, and social conditions.</div>
  </div>
  <div class="controls">
    <div class="clockbox">◷ Time <b id="time-display" style="color:var(--mint);font-size:13px;">06:00</b></div>
    <div class="clockbox">Weather <b id="weather-display" style="color:var(--gold);font-size:13px;">Sunny ☀️</b></div>
    <div class="speed-group">
      <button class="speed-btn active" data-speed="1">1×</button>
      <button class="speed-btn" data-speed="2">2×</button>
      <button class="speed-btn" data-speed="5">5×</button>
    </div>
    <button id="toggle-sim-btn" class="toggle">Ⅱ Pause</button>
  </div>
</header>

<section class="metrics">
  <div class="metric"><div class="metrichead"><span>Village Mood</span><span>😊</span></div><div class="metricvalue" id="avg-mood-metric">85%</div><div class="metricfoot">Average composite happiness</div></div>
  <div class="metric" id="economy"><div class="metrichead"><span>Total Economy</span><span>◈</span></div><div class="metricvalue" id="economy-display">300 🪙</div><div class="metricfoot">Tokens in circulation</div></div>
  <div class="metric"><div class="metrichead"><span>Tax Pool</span><span>🏛️</span></div><div class="metricvalue yellow" id="bank-metric">100</div><div class="metricfoot">Funds public services</div></div>
  <div class="metric"><div class="metrichead"><span>Critical Needs</span><span>⚠️</span></div><div class="metricvalue" style="color:var(--red)" id="interrupts-metric">0</div><div class="metricfoot">System 2 override events</div></div>
</section>

<section class="layout">
  <div class="panel flex flex-col" id="map">
    <div class="panelhead">
      <div><h2>Spatial Map & Resident Status</h2><p>Live tracking of agent locations, physical needs, and overall mood states</p></div>
      <span class="pill">LIVE SIMULATION</span>
    </div>
    
    <div id="canvas-container">
      <svg class="map-svg" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" viewBox="0 0 800 500" style="background-color: #13252f;">
        <defs>
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#294252" stroke-width="0.5" stroke-opacity="0.3"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)" />

        <g transform="translate(40, 25)">
          <rect width="280" height="125" fill="#334155" fill-opacity="0.4" stroke="#334155" stroke-width="2" rx="8"/>
          <text x="140" y="70" fill="#e8f1f7" font-size="14" font-weight="600" text-anchor="middle" letter-spacing="1">Residential Sector</text>
        </g>
        <g transform="translate(440, 25)">
          <rect width="320" height="125" fill="#166534" fill-opacity="0.4" stroke="#166534" stroke-width="2" rx="8"/>
          <text x="160" y="70" fill="#e8f1f7" font-size="14" font-weight="600" text-anchor="middle" letter-spacing="1">Community Farm</text>
        </g>
        <g transform="translate(40, 175)">
          <rect width="200" height="100" fill="#064e3b" fill-opacity="0.4" stroke="#064e3b" stroke-width="2" rx="8"/>
          <text x="100" y="55" fill="#e8f1f7" font-size="13" font-weight="600" text-anchor="middle" letter-spacing="1">Whispering Woods</text>
        </g>
        <g transform="translate(280, 175)">
          <rect width="240" height="100" fill="#475569" fill-opacity="0.4" stroke="#475569" stroke-width="2" rx="8"/>
          <text x="120" y="55" fill="#e8f1f7" font-size="13" font-weight="600" text-anchor="middle" letter-spacing="1">Town Square</text>
        </g>
        <g transform="translate(560, 175)">
          <rect width="200" height="100" fill="#0f766e" fill-opacity="0.4" stroke="#0f766e" stroke-width="2" rx="8"/>
          <text x="100" y="55" fill="#e8f1f7" font-size="13" font-weight="600" text-anchor="middle" letter-spacing="1">Schoolhouse</text>
        </g>
        <g transform="translate(40, 300)">
          <rect width="240" height="150" fill="#7f1d1d" fill-opacity="0.4" stroke="#7f1d1d" stroke-width="2" rx="8"/>
          <text x="120" y="80" fill="#e8f1f7" font-size="14" font-weight="600" text-anchor="middle" letter-spacing="1">Workshop</text>
        </g>
        <g transform="translate(320, 300)">
          <rect width="200" height="150" fill="#854d0e" fill-opacity="0.4" stroke="#854d0e" stroke-width="2" rx="8"/>
          <text x="100" y="80" fill="#e8f1f7" font-size="14" font-weight="600" text-anchor="middle" letter-spacing="1">Market Bazaar</text>
        </g>
        <g transform="translate(560, 300)">
          <rect width="200" height="150" fill="#312e81" fill-opacity="0.4" stroke="#312e81" stroke-width="2" rx="8"/>
          <text x="100" y="80" fill="#e8f1f7" font-size="14" font-weight="600" text-anchor="middle" letter-spacing="1">The Tavern</text>
        </g>
      </svg>
      
      <canvas id="simCanvas"></canvas>
      <div class="rain-overlay"></div>
    </div>
    
    <div id="agent-grid-container" class="agent-grid">
      <!-- Agent cards injected via JS -->
    </div>
  </div>
  
  <div class="panel logpanel" id="memory">
    <div class="logtop">
      <div><h2>Cognitive & Emotion Log</h2><p>Actions driven by routines, needs, and mood</p></div>
      <span class="pill">AUTO-SCROLL</span>
    </div>
    <div id="log-content" class="log-container">
      <!-- Logs injected via JS -->
    </div>
  </div>
</section>
</main>

<aside class="right-sidebar">
  <div style="padding-bottom: 12px; border-bottom: 1px solid var(--line);">
    <h2 style="font-size: 14px; margin: 0; font-weight: 600;">Backend Controls</h2>
  </div>
  
  <div>
    <label class="control-label">LLM Reasoning Engine</label>
    <select class="control-select">
      <option>Local Browser Engine</option>
      <option>Cloud Inference (Mock)</option>
    </select>
  </div>
  
  <div style="display: flex; flex-direction: column; gap: 10px; margin-top: auto;">
    <button class="control-btn" onclick="alert('Export: Dialogue logs downloaded to CSV.')">Export Logs to CSV</button>
    <button id="force-weather-btn" class="control-btn danger">Force Rain Event</button>
  </div>
</aside>
</div>

<script>
const config = {
    realSecondsPerHour: 5,
    tickRateMs: 50,
    timeScale: 0
};
config.timeScale = 60 / (config.realSecondsPerHour * 1000); 

const state = {
    isRunning: true,
    virtualTimeMins: 6 * 60,
    weather: 'Sunny',
    lastWeatherChangeHour: 6,
    lastEconomyHour: -1, 
    simSpeedMultiplier: 1,
    bankTokens: 100, 
    totalInterrupts: 0
};

const canvas = document.getElementById('simCanvas');
const ctx = canvas.getContext('2d');
const container = document.getElementById('canvas-container');

function resizeCanvas() {
    canvas.width = container.clientWidth;
    canvas.height = container.clientHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas(); // Initial call

const zones = {
    'Residential': { x: 0.05, y: 0.05, w: 0.35, h: 0.25, color: '#334155', label: 'Residential Sector' },
    'Farm':        { x: 0.55, y: 0.05, w: 0.40, h: 0.25, color: '#166534', label: 'Community Farm' },
    'Commons':     { x: 0.35, y: 0.35, w: 0.30, h: 0.20, color: '#475569', label: 'Town Square' },
    'School':      { x: 0.70, y: 0.35, w: 0.25, h: 0.20, color: '#0f766e', label: 'Schoolhouse' },
    'Forest':      { x: 0.05, y: 0.35, w: 0.25, h: 0.20, color: '#064e3b', label: 'Whispering Woods' },
    'Workshop':    { x: 0.05, y: 0.60, w: 0.30, h: 0.30, color: '#7f1d1d', label: 'Workshop' },
    'Market':      { x: 0.40, y: 0.60, w: 0.25, h: 0.30, color: '#854d0e', label: 'Market Bazaar' },
    'Tavern':      { x: 0.70, y: 0.60, w: 0.25, h: 0.30, color: '#312e81', label: 'The Tavern' }
};

function getZoneCenter(zoneKey) {
    const z = zones[zoneKey];
    return {
        x: (z.x + z.w / 2) * canvas.width,
        y: (z.y + z.h / 2) * canvas.height
    };
}

class Agent {
    constructor(id, name, role, color, startZone, traits) {
        this.id = id;
        this.name = name;
        this.role = role;
        this.color = color;
        this.currentZone = startZone;
        this.traits = traits;
        
        const startPos = getZoneCenter(startZone);
        this.x = startPos.x;
        this.y = startPos.y;
        this.targetX = startPos.x;
        this.targetY = startPos.y;
        
        this.currentTask = 'Sleeping';
        this.system2Override = null; 
        this.lastProcessedHour = -1;
        this.isMoving = false;
        
        this.needs = {
            hunger: 80 + Math.random() * 20,
            thirst: 80 + Math.random() * 20,
            energy: 100,
            hygiene: 90 + Math.random() * 10,
            social: 70 + Math.random() * 30
        };
        
        this.tokens = 20; 
        this.productivity = 1.0; 
        this.inventory = { rawFood: 0, wood: 0, meals: 2, tools: 0 };
        this.moodScore = 85;
        this.emotion = '😊';
    }

    update(dt) {
        const dx = this.targetX - this.x;
        const dy = this.targetY - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        
        if (dist > 1) {
            this.isMoving = true;
            let speedMod = this.needs.energy < 30 ? 0.6 : 1; 
            const speed = 120 * (dt / 1000) * speedMod; 
            const moveDist = Math.min(speed, dist);
            this.x += (dx / dist) * moveDist;
            this.y += (dy / dist) * moveDist;
        } else {
            this.isMoving = false;
            this.x = this.targetX;
            this.y = this.targetY;
        }
    }

    moveTo(zoneKey) {
        if (this.currentZone === zoneKey) return;
        this.currentZone = zoneKey;
        
        const z = zones[zoneKey];
        const maxOffsetX = (z.w * canvas.width) * 0.25;
        const maxOffsetY = (z.h * canvas.height) * 0.25;
        
        const center = getZoneCenter(zoneKey);
        this.targetX = center.x + (Math.random() * maxOffsetX * 2 - maxOffsetX);
        this.targetY = center.y + (Math.random() * maxOffsetY * 2 - maxOffsetY);
    }

    updateNeeds(virtualMinsElapsed, zoneOccupants) {
        const decayBase = (virtualMinsElapsed / 60) * 5; 
        const isResting = this.currentTask === 'Sleeping' || this.currentTask.includes('Resting');
        const metabolicRate = isResting ? 0.3 : 1.0; 
        
        this.needs.hunger = Math.max(0, this.needs.hunger - (decayBase * 1.5 * metabolicRate));
        this.needs.thirst = Math.max(0, this.needs.thirst - (decayBase * 2.0 * metabolicRate));
        this.needs.hygiene = Math.max(0, this.needs.hygiene - decayBase * 0.5);
        this.needs.social = Math.max(0, this.needs.social - decayBase * 0.8);

        if (!isResting) {
            this.needs.energy = Math.max(0, this.needs.energy - decayBase * 1.2);
        }

        if (!this.isMoving) {
            const regenRate = (virtualMinsElapsed / 60) * 30; 
            
            if (isResting) {
                this.needs.energy = Math.min(100, this.needs.energy + regenRate * 2.5);
                this.needs.hygiene = Math.min(100, this.needs.hygiene + regenRate * 0.5); 
            }
            
            if (this.currentZone === 'Tavern') {
                if(this.currentTask.includes('Eating') || this.currentTask.includes('Drinking') || this.currentTask.includes('Shelter')) {
                   this.needs.hunger = Math.min(100, this.needs.hunger + regenRate);
                   this.needs.thirst = Math.min(100, this.needs.thirst + regenRate);
                }
            }

            // Social system based on crowd proximity
            if (zoneOccupants > 1) {
                const socialBoost = regenRate * 0.6 * (zoneOccupants - 1);
                this.needs.social = Math.min(100, this.needs.social + socialBoost);
            }
        }
    }

    updateEmotion() {
        // --- HOLISTIC EMOTION ALGORITHM ---
        // 1. Physical Health Score (Average of all biological needs)
        const physicalScore = (this.needs.hunger + this.needs.thirst + this.needs.energy + this.needs.hygiene) / 4;
        
        // 2. Economic Status (Baseline 30 tokens = 100% economic security)
        const economicScore = Math.min(100, (this.tokens / 30) * 100);
        
        // 3. Social Fulfillment
        const socialScore = this.needs.social;
        
        // Weighted composite overall mood score
        this.moodScore = (physicalScore * 0.5) + (socialScore * 0.2) + (economicScore * 0.3);

        // Immediate overrides based on critical survival states
        if (this.needs.hunger < 15 || this.needs.thirst < 15) {
            this.emotion = '😫'; // Suffering
        } else if (this.needs.energy < 15) {
            this.emotion = '😴'; // Exhausted
        } else if (this.tokens < 2 && this.needs.hunger < 50) {
            this.emotion = '😰'; // Financial panic
        } else {
            // General mood mapping
            if (this.moodScore > 80) this.emotion = '🤩'; // Thriving
            else if (this.moodScore > 60) this.emotion = '😊'; // Happy
            else if (this.moodScore > 40) this.emotion = '😐'; // Okay
            else if (this.moodScore > 25) this.emotion = '😟'; // Stressed
            else this.emotion = '😭'; // Miserable
        }
    }

    getRoutine(hour) {
        if (hour < 6 || hour >= 22) return { zone: 'Residential', task: 'Sleeping' };
        
        const schedule = {
            'Blacksmith': { 6: { z: 'Residential', t: 'Morning Prep' }, 8: { z: 'Workshop', t: 'Forging Tools' }, 13: { z: 'Market', t: 'Buying Scrap' }, 15: { z: 'Workshop', t: 'Repairing Armor' }, 18: { z: 'Tavern', t: 'Evening Drinks' }},
            'Farmer': { 6: { z: 'Farm', t: 'Watering Crops' }, 11: { z: 'Market', t: 'Selling Produce' }, 14: { z: 'Farm', t: 'Harvesting' }, 19: { z: 'Commons', t: 'Socializing' }},
            'Merchant': { 6: { z: 'Market', t: 'Setting up Stall' }, 9: { z: 'Market', t: 'Trading Goods' }, 17: { z: 'Tavern', t: 'Counting Coins' }},
            'Builder': { 6: { z: 'Workshop', t: 'Gathering Timber' }, 9: { z: 'Commons', t: 'Fixing Fountain' }, 14: { z: 'Residential', t: 'Repairing Roofs' }, 19: { z: 'Tavern', t: 'Resting' }},
            'Medic': { 6: { z: 'Commons', t: 'Morning Clinic' }, 12: { z: 'Farm', t: 'Gathering Herbs' }, 15: { z: 'Commons', t: 'Treating Patients' }, 20: { z: 'Residential', t: 'Reading' }},
            'Cook': { 6: { z: 'Market', t: 'Buying Ingredients' }, 9: { z: 'Tavern', t: 'Prep Cooking' }, 12: { z: 'Tavern', t: 'Serving Lunch' }, 17: { z: 'Tavern', t: 'Serving Dinner' }},
            'Courier': { 6: { z: 'Market', t: 'Collecting Mail' }, 9: { z: 'Residential', t: 'Delivering Parcels' }, 13: { z: 'Farm', t: 'Running Errands' }, 16: { z: 'Workshop', t: 'Delivering Supplies' }, 19: { z: 'Commons', t: 'Resting' }},
            'Teacher': { 6: { z: 'School', t: 'Lesson Planning' }, 8: { z: 'School', t: 'Teaching Math' }, 12: { z: 'Commons', t: 'Recess Duty' }, 13: { z: 'School', t: 'Teaching History' }, 17: { z: 'Residential', t: 'Grading Papers' }},
            'Guard': { 6: { z: 'Commons', t: 'Morning Patrol' }, 10: { z: 'Market', t: 'Watching Crowd' }, 14: { z: 'Forest', t: 'Perimeter Check' }, 18: { z: 'Tavern', t: 'Keeping Peace' }},
            'Forester': { 6: { z: 'Forest', t: 'Chopping Wood' }, 12: { z: 'Workshop', t: 'Delivering Logs' }, 14: { z: 'Forest', t: 'Scouting Trails' }, 19: { z: 'Tavern', t: 'Trading Pelts' }}
        };

        const roleSchedule = schedule[this.role];
        let currentActivity = roleSchedule[6]; 
        
        for (const [h, act] of Object.entries(roleSchedule)) {
            if (hour >= parseInt(h)) {
                currentActivity = act;
            }
        }
        
        return { zone: currentActivity.z, task: currentActivity.t };
    }

    executeCognitiveLoop(hour, weather) {
        if (this.lastProcessedHour === hour) return;
        this.lastProcessedHour = hour;

        if (this.system2Override) {
            if (this.system2Override === 'Eating' && this.needs.hunger > 80 && this.needs.thirst > 80) this.system2Override = null;
            else if (this.system2Override === 'Resting' && this.needs.energy > 80) this.system2Override = null;
        }

        let isSystem2 = false;
        let actionReason = "";
        
        let routine = this.getRoutine(hour);
        let targetZone = routine.zone;
        this.currentTask = routine.task;
        actionReason = `Scheduled task: ${this.currentTask}`;

        if (this.needs.hunger < 25 || this.needs.thirst < 25) {
            isSystem2 = true;
            targetZone = 'Tavern';
            this.currentTask = 'Emergency Eating/Drinking';
            this.system2Override = 'Eating';
            actionReason = "Critically hungry/thirsty. Seeking Tavern.";
            state.totalInterrupts++;
        }
        else if (this.needs.energy < 20) {
            isSystem2 = true;
            targetZone = 'Residential';
            this.currentTask = 'Emergency Resting';
            this.system2Override = 'Resting';
            actionReason = "Exhausted. Abandoning schedule to sleep.";
            state.totalInterrupts++;
        }
        else if (weather === 'Raining' && (targetZone === 'Farm' || targetZone === 'Commons' || targetZone === 'Market')) {
            isSystem2 = true;
            targetZone = 'Tavern';
            this.currentTask = 'Seeking Shelter';
            actionReason = "Raining. Seeking indoor shelter.";
        }
        else if (this.system2Override) {
            isSystem2 = true;
            targetZone = this.system2Override === 'Eating' ? 'Tavern' : 'Residential';
            this.currentTask = `Recovering (${this.system2Override})`;
            actionReason = "Continuing recovery of critical needs.";
        }

        if (this.currentZone !== targetZone) {
            this.moveTo(targetZone);
        }

        if (isSystem2 || hour === 8) {
            this.logCognition(hour, weather, targetZone, actionReason, isSystem2);
        }
        
        document.getElementById('interrupts-metric').innerText = state.totalInterrupts;
    }

    logCognition(hour, weather, targetZone, reason, isSystem2) {
        const timeStr = `${hour.toString().padStart(2, '0')}:00`;
        const entryClass = isSystem2 ? 'system2' : 'system1';
        const typeLabel = isSystem2 ? 'SYS2_INTERRUPT' : 'SYS1_ROUTINE';
        const perceptionText = `H:${Math.round(this.needs.hunger)} | E:${Math.round(this.needs.energy)} | Mood: ${Math.round(this.moodScore)}`;
        
        const html = `
            <div class="log-entry ${entryClass}">
                <div class="flex justify-between items-center mb-1">
                    <strong style="color: ${this.color}">${this.name} <span class="text-slate-400 font-normal text-xs">(${this.role})</span></strong>
                    <span class="text-xs opacity-70">${timeStr} | ${typeLabel}</span>
                </div>
                <div class="space-y-0.5 mt-2">
                    <div class="flex"><span class="w-12 shrink-0 text-blue-400">STATE:</span> <span class="text-slate-300">${perceptionText}</span></div>
                    <div class="flex"><span class="w-12 shrink-0 text-purple-400">PLAN:</span> <span class="text-slate-300">${reason} → ${zones[targetZone].label}</span></div>
                </div>
            </div>
        `;
        
        addLog(html);
    }
}

function addLog(html) {
    const logContainer = document.getElementById('log-content');
    logContainer.insertAdjacentHTML('beforeend', html);
    if (logContainer.children.length > 50) logContainer.removeChild(logContainer.firstChild); 
    logContainer.scrollTop = logContainer.scrollHeight;
}

const agents = [
    new Agent('a1', 'Elias', 'Blacksmith', '#ef4444', 'Residential', 'Fixes the village tools.'),
    new Agent('a2', 'Clara', 'Farmer', '#22c55e', 'Residential', 'Grows the food.'),
    new Agent('a3', 'Silas', 'Merchant', '#3b82f6', 'Residential', 'Trades goods and coins.'),
    new Agent('a4', 'Mira', 'Builder', '#f97316', 'Residential', 'Constructs and repairs.'),
    new Agent('a5', 'Nikhil', 'Medic', '#ec4899', 'Residential', 'Heals the sick.'),
    new Agent('a6', 'Tara', 'Cook', '#eab308', 'Residential', 'Prepares community meals.'),
    new Agent('a7', 'Dev', 'Courier', '#06b6d4', 'Residential', 'Delivers messages rapidly.'),
    new Agent('a8', 'Leela', 'Teacher', '#a855f7', 'Residential', 'Educates the youth.'),
    new Agent('a9', 'Arjun', 'Guard', '#94a3b8', 'Residential', 'Patrols and protects.'),
    new Agent('a10', 'Pia', 'Forester', '#14b8a6', 'Residential', 'Manages woodland resources.'),
    new Agent('a11', 'Ravi', 'Farmer', '#4ade80', 'Residential', 'Tends to the outer fields.'),
    new Agent('a12', 'Kael', 'Guard', '#64748b', 'Residential', 'Secures the gates.'),
    new Agent('a13', 'Lyra', 'Builder', '#fdba74', 'Residential', 'Designs new homes.'),
    new Agent('a14', 'Jace', 'Forester', '#2dd4bf', 'Residential', 'Scouts the deep woods.'),
    new Agent('a15', 'Anya', 'Cook', '#fde047', 'Residential', 'Bakes the daily bread.')
];

function executeTransaction(buyer, seller, price, itemKey) {
    const tax = price * 0.10; 
    const net = price - tax;
    
    buyer.tokens -= price;
    seller.tokens += net;
    state.bankTokens += tax;
    
    buyer.inventory[itemKey] += 1;
    seller.inventory[itemKey] -= 1;
}

function processEconomyCycle(hour) {
    if (state.lastEconomyHour === hour) return;
    state.lastEconomyHour = hour;

    if (hour === 14) {
        addLog(`<div class="log-entry economy text-center font-bold text-yellow-400">--- DAILY PRODUCTION PHASE ---</div>`);
        agents.forEach(a => {
            const output = Math.floor(2 * a.productivity); 
            if (a.role === 'Farmer') a.inventory.rawFood += output;
            if (a.role === 'Forester') a.inventory.wood += output;
            
            if (a.role === 'Cook' && a.inventory.rawFood > 0) {
                a.inventory.meals += a.inventory.rawFood;
                a.inventory.rawFood = 0;
            }
            if (a.role === 'Blacksmith' && a.inventory.wood > 0) {
                a.inventory.tools += a.inventory.wood;
                a.inventory.wood = 0;
            }
        });
    }

    if (hour === 17) {
        addLog(`<div class="log-entry economy text-center font-bold text-yellow-400">--- MARKET & SERVICES PHASE ---</div>`);
        
        const publicRoles = ['Guard', 'Medic', 'Teacher', 'Courier', 'Builder', 'Merchant'];
        publicRoles.forEach(role => {
            let servants = agents.filter(a => a.role === role);
            servants.forEach(servant => {
                if (state.bankTokens >= 5) {
                    state.bankTokens -= 5;
                    servant.tokens += 5;
                }
            });
        });

        let farmers = agents.filter(a => a.role === 'Farmer');
        let cooks = agents.filter(a => a.role === 'Cook');
        let foresters = agents.filter(a => a.role === 'Forester');
        let smiths = agents.filter(a => a.role === 'Blacksmith');

        farmers.forEach(farmer => {
            cooks.forEach(cook => {
                while(farmer.inventory.rawFood > 0 && cook.tokens >= 2) executeTransaction(cook, farmer, 2, 'rawFood');
            });
        });

        foresters.forEach(forester => {
            smiths.forEach(smith => {
                while(forester.inventory.wood > 0 && smith.tokens >= 3) executeTransaction(smith, forester, 3, 'wood');
            });
        });

        agents.forEach(a => {
            let activeCook = cooks.find(c => c.inventory.meals > 0);
            if (a.role !== 'Cook' && a.inventory.meals < 1 && a.tokens >= 5 && activeCook) {
                executeTransaction(a, activeCook, 5, 'meals');
            }
            
            let activeSmith = smiths.find(s => s.inventory.tools > 0);
            if (a.role !== 'Blacksmith' && a.inventory.tools < 1 && a.tokens >= 8 && activeSmith) {
                executeTransaction(a, activeSmith, 8, 'tools');
                a.productivity = 1.2; 
            }
        });
    }

    if (hour === 20) {
        addLog(`<div class="log-entry economy text-center font-bold text-yellow-400">--- CONSUMPTION PHASE ---</div>`);
        agents.forEach(a => {
            if (a.inventory.meals > 0) {
                a.inventory.meals -= 1;
                a.needs.hunger = 100;
                a.needs.energy = 100;
                if (a.productivity < 1.0) a.productivity = 1.0; 
            } else {
                a.needs.hunger -= 20;
                a.needs.energy -= 10;
                a.productivity = 0.5; 
                addLog(`<div class="log-entry system2"><strong class="text-red-400">⚠️ Starvation:</strong> ${a.name} could not afford food. Productivity halved.</div>`);
            }

            if (a.inventory.tools > 0 && Math.random() < 0.3) {
                a.inventory.tools -= 1;
                if(a.inventory.tools === 0) a.productivity = 1.0; 
            }
        });
    }
}

function getNeedColor(val) {
    if(val > 60) return '#63e6be'; 
    if(val > 25) return '#ffc86a'; 
    return '#ff6b6b'; 
}

function getMoodColor(val) {
    if(val > 70) return '#63e6be';
    if(val > 40) return '#69b7ff';
    if(val > 20) return '#ffc86a';
    return '#ff6b6b';
}

function updateAgentCardsUI() {
    const container = document.getElementById('agent-grid-container');
    if (!container) return;
    
    container.innerHTML = agents.map(a => `
        <div class="agent-card">
            <div class="flex justify-between items-center mb-1">
                <span class="font-bold text-[12px]" style="color: ${a.color}">${a.name} <span class="text-[9px] text-slate-400 font-normal">(${a.role})</span></span>
                <span class="text-base" title="Current Emotion">${a.emotion}</span>
            </div>
            
            <div class="text-[9px] text-slate-300 bg-slate-900/60 p-1 rounded truncate border border-slate-700/50">
                <span class="text-blue-300">Task:</span> ${a.currentTask}
            </div>
            
            <div class="w-full mt-1 mb-1">
                <div class="flex justify-between text-[9px] text-slate-400"><span>Mood Score</span><span>${Math.round(a.moodScore)}/100</span></div>
                <div class="mood-bar"><div class="mood-fill" style="width: ${a.moodScore}%; background: ${getMoodColor(a.moodScore)}"></div></div>
            </div>
            
            <div class="needs-bars">
                <div class="need-row">
                    <span class="w-8">Health</span>
                    <div class="need-track"><div class="need-fill ${a.needs.hunger < 25 ? 'critical' : ''}" style="width: ${a.needs.hunger}%; background: ${getNeedColor(a.needs.hunger)}"></div></div>
                </div>
                <div class="need-row">
                    <span class="w-8">Energy</span>
                    <div class="need-track"><div class="need-fill ${a.needs.energy < 25 ? 'critical' : ''}" style="width: ${a.needs.energy}%; background: ${getNeedColor(a.needs.energy)}"></div></div>
                </div>
                <div class="need-row">
                    <span class="w-8">Social</span>
                    <div class="need-track"><div class="need-fill" style="width: ${a.needs.social}%; background: ${getNeedColor(a.needs.social)}"></div></div>
                </div>
            </div>

            <div class="inv-bar mt-1">
                <span>🍔 ${a.inventory.meals}</span>
                <span>🌾 ${a.inventory.rawFood}</span>
                <span>🪵 ${a.inventory.wood}</span>
                <span>⚒️ ${a.inventory.tools}</span>
            </div>
            
            <div class="mt-1 flex justify-between items-center text-[9px]">
                <div class="flex items-center text-slate-400 truncate max-w-[70px]">
                    <span class="w-1.5 h-1.5 rounded-full mr-1.5 shrink-0" style="background-color: ${zones[a.currentZone].color}"></span>
                    <span class="truncate">${zones[a.currentZone].label}</span>
                </div>
                <span class="text-yellow-400 font-mono font-bold text-[10px]">${a.tokens.toFixed(1)} 🪙</span>
            </div>
        </div>
    `).join('');
}

function updateEnvironment(dt) {
    if (!state.isRunning) return;

    const effectiveDt = dt * state.simSpeedMultiplier;
    const virtualMinsElapsed = effectiveDt * config.timeScale;
    
    state.virtualTimeMins += virtualMinsElapsed;
    if (state.virtualTimeMins >= 24 * 60) {
        state.virtualTimeMins = 0;
    }
    const currentHour = Math.floor(state.virtualTimeMins / 60) % 24;

    let hrs = currentHour;
    let mins = Math.floor(state.virtualTimeMins % 60);
    const timeStr = `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}`;
    
    document.getElementById('time-display').innerText = timeStr;

    if (currentHour !== state.lastWeatherChangeHour && currentHour % 3 === 0) {
        state.lastWeatherChangeHour = currentHour;
        if (Math.random() < 0.15) {
            state.weather = state.weather === 'Sunny' ? 'Raining' : 'Sunny';
            const wDisplay = document.getElementById('weather-display');
            if (state.weather === 'Raining') {
                wDisplay.innerHTML = 'Raining 🌧️';
                wDisplay.className = 'font-semibold text-blue-400';
                container.classList.add('raining');
            } else {
                wDisplay.innerHTML = 'Sunny ☀️';
                wDisplay.className = 'font-semibold text-yellow-400';
                container.classList.remove('raining');
            }
        }
    }

    processEconomyCycle(currentHour);

    let zoneOccupancy = {};
    agents.forEach(a => {
        if (!a.isMoving) zoneOccupancy[a.currentZone] = (zoneOccupancy[a.currentZone] || 0) + 1;
    });

    let totalTokens = state.bankTokens;
    let totalMood = 0;
    
    agents.forEach(agent => {
        let occupantsInZone = zoneOccupancy[agent.currentZone] || 0;
        agent.updateNeeds(virtualMinsElapsed, occupantsInZone);
        agent.updateEmotion();
        agent.executeCognitiveLoop(currentHour, state.weather);
        
        totalTokens += agent.tokens;
        totalMood += agent.moodScore;
    });

    document.getElementById('economy-display').innerHTML = `<span class="text-white">${Math.round(totalTokens)}</span> 🪙`;
    document.getElementById('avg-mood-metric').innerText = `${Math.round(totalMood / agents.length)}%`;
    document.getElementById('bank-metric').innerText = Math.round(state.bankTokens);

    if (Math.random() < 0.1) {
        updateAgentCardsUI();
    }
}

const agentSvgPath = new Path2D("M 0 -2 C -5 -2 -8 3 -8 10 L 8 10 C 8 3 5 -2 0 -2 Z M 0 -10 A 4 4 0 1 1 0 -2 A 4 4 0 1 1 0 -10 Z");

function drawAgents(dt) {
    const effectiveDt = dt * state.simSpeedMultiplier;
    
    agents.forEach(agent => {
        if(state.isRunning) agent.update(effectiveDt);

        if (agent.isMoving) {
            ctx.beginPath();
            ctx.moveTo(agent.x, agent.y);
            ctx.lineTo(agent.targetX, agent.targetY);
            ctx.strokeStyle = agent.color;
            ctx.globalAlpha = 0.4;
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 4]);
            ctx.stroke();
            ctx.setLineDash([]);
        }

        ctx.globalAlpha = 1.0;
        
        ctx.save();
        ctx.translate(agent.x, agent.y);

        ctx.beginPath();
        ctx.ellipse(0, 10, 8, 3, 0, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(0,0,0,0.5)';
        ctx.fill();

        ctx.fillStyle = agent.color;
        ctx.fill(agentSvgPath); 
        
        ctx.lineWidth = 1.5;
        ctx.strokeStyle = '#ffffff';
        ctx.stroke(agentSvgPath);

        ctx.restore();

        ctx.fillStyle = '#f8fafc';
        ctx.font = '600 9px Inter';
        ctx.textAlign = 'center';
        ctx.fillText(agent.name, agent.x, agent.y - 14);
        
        if (agent.emotion !== '😊') {
            ctx.font = '12px Inter';
            ctx.fillText(agent.emotion, agent.x, agent.y - 24);
        }
    });
}

let lastTime = performance.now();
function loop(timestamp) {
    const dt = timestamp - lastTime;
    lastTime = timestamp;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    updateEnvironment(dt);
    drawAgents(dt);

    requestAnimationFrame(loop);
}

document.getElementById('toggle-sim-btn').addEventListener('click', (e) => {
    state.isRunning = !state.isRunning;
    if (state.isRunning) {
        e.target.innerText = 'Ⅱ Pause';
        e.target.style.background = '#2776bb';
    } else {
        e.target.innerText = '▶ Resume';
        e.target.style.background = '#16a34a';
    }
});

document.querySelectorAll('.speed-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        document.querySelectorAll('.speed-btn').forEach(b => {
            b.classList.remove('active');
            b.style.color = 'var(--muted)';
        });
        e.target.classList.add('active');
        e.target.style.color = '#fff';
        state.simSpeedMultiplier = parseInt(e.target.getAttribute('data-speed'));
    });
});

document.getElementById('force-weather-btn').addEventListener('click', () => {
    state.weather = 'Raining';
    const wDisplay = document.getElementById('weather-display');
    wDisplay.innerHTML = 'Raining 🌧️';
    wDisplay.className = 'font-semibold text-blue-400';
    container.classList.add('raining');
});

updateAgentCardsUI();
requestAnimationFrame(loop);
</script>
</body>
</html>
"""

components.html(html_source, height=1200, scrolling=True)