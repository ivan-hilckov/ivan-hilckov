# Ivan Hilkov

**Lead Fullstack Engineer** — Moscow, Russia (UTC+3)

## Contact

- **Email:** strange.mole@gmail.com
- **Telegram:** @mrbzzz
- **LinkedIn:** linkedin.com/in/ivan-hilkov-a1022154/
- **GitHub:** github.com/ivan-hilckov

## Professional Summary

Lead Fullstack Engineer with 17+ years building high‑load web applications with React/Next.js and data‑intensive UIs. Deep experience across streaming/media and geospatial domains. Strong focus on pragmatic architecture, performance optimization, and end‑to‑end delivery. Led teams of up to 8 engineers, set up QA automation and CI/CD, and collaborated closely with product and QA for predictable releases. Remote‑first, immediate availability, open to international contract and invoicing.

## Core Competencies

- **Frontend:** React, Next.js, TypeScript, Redux, React Router, React Native, HTML, CSS, TailwindCSS, Webpack
- **Backend:** Node.js, FastAPI, Flask
- **Databases & Caching:** PostgreSQL, Redis
- **Geospatial & Media:** Cesium, Mapbox, Leaflet, Potree, Pannellum, FFmpeg, HLS
- **Quality & Tooling:** Git, Docker, CI/CD, Cypress, Jest
- **Practices:** Agile, Scrum; performance optimization; accessibility; frontend architecture

## Selected Achievements

- **START:** Cut API latency by ~40% during peak traffic through query and caching optimizations.
- **Skyeer:** Co‑designed QA automation (800+ Selenium E2E tests) with QA team; release stability improved by ~80%.
- **Skyeer:** Delivered platform MVP in 3 months; 1st place at Gazprom “Unmanned Biathlon” (measurement accuracy ±0.02 m³).
- **Skyeer:** Implemented resumable uploads up to 100 GB via tus.io with pause/resume support.

## Professional Experience

### **HRONIKA** — Co‑Founder / Fullstack Engineer — _Apr 2025 — Present_ — Moscow

Product: Autonomous timelapse system for construction/infrastructure monitoring.

- Built prototype on Raspberry Pi 4 + Canon 1100D with LTE connectivity and UPS HAT + Li‑ion in IP67 enclosure; solar‑ready.
- Frontend: React, HeroUI, TailwindCSS (camera dashboard, photo viewing, timelapse generation); E2E tests in Cypress.
- Backend: FastAPI with task queues (Celery + Redis), REST API for auth, camera, photo, timelapse management.
- Authored technical documentation and public roadmap; submitted application to Sber500 accelerator.
- Site: hronika.tech

### **START** — Lead Frontend Engineer — _Jan 2023 — May 2024_ — Moscow

Domain: Streaming/media; Smart TV and web platform.

- Built new sections in Next.js: “Movies on TV” and “TV Series”, including player and TV channel storefront integration.
- Shipped the TV section with program schedules and catch‑up TV (viewing past programs).
- Refactored channel viewing pages, improving navigation and UX.
- Maintained and extended admin editor (React + Bootstrap) and generated Open Graph metadata server‑side (SSR).
- Optimized user queries and caching to reduce server load during peaks; latency reduced by ~40% in specific high‑traffic events.
- Improved lazy‑loading of home page previews and dynamic feeds with infinite scroll; implemented banner grid fed by REST API.
- Refactored FAQ and support contact flow; redesigned login and subscription checkout.
- Reworked monolithic payment form by extracting business logic/state to Redux for readability and reuse.
- Streamlined A/B testing system to speed up experimental feature rollout.
- Led and mentored 4 frontend engineers; task estimation, architecture, onboarding, and daily syncs.
- Link: start.ru — Example page: start.ru/archive/tvmovie

### **Tvigle** — Lead Frontend Engineer — _May 2024 — Oct 2024_ — Moscow

Domain: Online cinema.

- Maintained existing video player (JavaScript, jQuery); integrated ad SDKs (Yandex Ads, VK Ads) via MRAID.
- Refactored ad module to support VAST 4.0 (from 2.0).
- Adapted online cinema layout for mobile devices.
- Built mobile application using React Native (Android/iOS support).
- Performed code review and audit for the main Next.js project.

### **Skyeer** — Lead Frontend Engineer — _Apr 2017 — Jan 2023_ — Moscow

Product line: Web‑GIS platform for UAV data analytics, photogrammetry automation, and domain solutions (construction, mining, logistics, landfills).

#### UAV Data Analytics Web Service — map.skyeermap.com

Cloud platform for spatial data analysis and object monitoring. Integrates drone data and geodetic measurements to assess material volumes and monitor object condition using 3D models and orthophotos.

- Delivered MVP in 3 months for Gazprom “Unmanned Biathlon” (1st place; accuracy ±0.02 m³) using React, Redux, Webpack, Leaflet.  
  Reference: skyeermap.com/blog/achivement/skyeer-luchshee-softvernoe-reshenie
- Evolved MVP to full web‑GIS product: React, Redux‑Saga, React Router, Mapbox, Potree, Recharts, TurfJS, proj4js, GDAL, Django REST Framework, tus.io, Puppeteer.
- Implemented user uploads up to 100 GB with resumable transfers (tus.io), pause/resume; formats: GeoTIFF, ECW, DXF, WMS, XYZ, Cesium Ion 3D, point clouds (Potree), SHP, KML, GeoJSON.
- Built layer comparison UI, survey date switching, basemap/projection selection, layer ordering and transparency.
- Added swipe comparison for multi‑date user layers and 360° panoramas using Pannellum; point cloud visualization via Potree.
- Tools for measurements: area, volume, slope, longitudinal profile, elevation points, markers, with draw/import for GeoJSON/WKT/KML/SHP.
- Export of measurements to XLSX/PDF; attachments upload (JPG, PNG, PDF, DOC, XLS, etc.).
- Role/access control (Project, Flight, Measurement): Manager, Pilot, View‑only, etc.
- Integrated CesiumJS for 3D with parity to Mapbox functionality.
- Authored a 50+ component UI library with a React Cosmos playground.
- Internationalization with i18next (English and German).
- Introduced Prettier/ESLint; >150 Jest tests with ~80% business‑logic coverage.
- Set up CI/CD pipeline, automated frontend testing, integration, and releases.
- Co‑implemented Selenium testing (800+ automated tests) with QA; release stability improved by ~80%.
- Hired 8 frontend engineers (Middle–Senior); onboarding and mentoring in a complex GIS domain.
- Established Agile practices: weekly sprints, daily standups, grooming, rolling releases, demos, retrospectives.
- Organized technical writing and documentation process (architecture, functionality, user scenarios).  
  Docs: doc.map.skyeermap.com

#### Automated Photogrammetry — attractor.aero

Automated service from UAV data upload to orthophoto, DTM, and point cloud.

- UI built on shared components from map.skyeermap.com; multilingual via i18next.
- Large‑volume image upload (10,000+ photos) via tus.io: bandwidth detection, parallel upload, pause/resume on interruptions.
- Displayed EXIF metadata; assembled minimal survey kit (DJI Mini 2, RTK GNSS Emlid).
- Wrote API requirements and formalized output data specs; prepared user and technical documentation.
- Implemented automated testing using Selenium; set up Prettier/ESLint.

#### Quarry Road Monitoring — NLMK IT (Habr article)

Automated assessment of quarry road conditions based on aerial photography and photogrammetry.

- Implemented in 2 months on a minimal stack: Django, DRF, jQuery, Bootstrap, Leaflet.
- Built prototype, coordinated solutions/UI with the client; tech supervision and process setup; authored user docs.  
  Article: habr.com/ru/companies/nlmk/articles/650419/

#### Linear Object Monitoring — aeroinspector.ru

Monitoring of linear objects with video archive and picket referencing.

- Advised on architecture for video + geodata specifics; prototyped video stream ↔ GPS log synchronization; formed the core team.

#### Waste Landfill Monitoring — reo.ru/flyby

Nationwide project for landfill monitoring using drones with laser scanners.

- Advised on architecture for 3D data and video documentation; formed the team; supported the project from prototype to release.

### **Amediateka.ru** — Senior Frontend Engineer — _Feb 2019 — Dec 2019_ — Moscow

SVOD platform.

- Built account support sections (FAQ, feedback); enhanced payment form and integrations using React/Redux.
- Implemented catalog pages on Next.js with SSR; content cards and episode switcher; extended player features (actor info, auto‑next, recommendations).
- Added Open Graph metadata for social previews; optimized builds with code splitting.

### **Ivideon (Cloud Video Surveillance)** — Senior Frontend Engineer — _Sep 2016 — Apr 2017_ — Moscow

- Extended UI/UX library with custom timeline and storyboard with event markers; adapted components for mobile.
- Evolved proprietary state management (Redux‑like) with async data loading; built account pages with design system components.
- Built an internal Canvas tool to annotate queues for ML training (automatic visitor counting).

### **REKOD (JSC NPK REKOD)** — Senior Frontend Engineer — _Feb 2016 — Sep 2016_ — Moscow

- SPA for WWII monuments monitoring/inspections with Create React App, React, React Router, Redux, Redux‑Saga.
- Mobile adaptation with Bootstrap/LESS; cartography module (React + Leaflet) for tracks and object meta.
- Photo upload/view with comments and on‑image annotations; React Native app with offline mode and sync on reconnect.
- White‑label architecture (theming, object schema/description via REST API) for re‑use; extended inspections with tasking and automated defect verification.

### **Liga Stavok** — Frontend Developer — _Sep 2015 — Jan 2016_ — Russia

- Built scalable UI/UX library of 40+ React components and a custom playground (Storybook‑like).
- LESS styling with dynamic variables/media queries; centralized state via Redux with dynamic slice import (code splitting and on‑demand state injection).
- Integrated ASP.NET REST API via Redux Thunk; migrated build from Gulp to Webpack (build time 20 → 1 minute; smaller bundles via split chunking).

### **OneTwoTrip** — Frontend Developer — _May 2015 — Sep 2015_ — Moscow

- Maintained jQuery payment module (5,000+ LOC); generated PDF tickets with PhantomJS.
- Implemented upsell/cross‑sell popups using REST API; optimized ticket search via static data preloading with Lua scripts.
- Built email campaign builder UI (Bootstrap); refactored payment form to React + Webpack; introduced Redux for complex state.
- Built landing pages with dynamic parameters via REST API; refactored search page with adaptive styling and full mobile support.

### **Sovzond** — Frontend Developer — _Jun 2013 — May 2015_ — Moscow

- Designed architecture and built the “Satellite Imagery Archive” SPA using BackboneJS and Bootstrap.
- Integrated REST API for dynamic satellite image search; built polygon drawing components (Leaflet.js).
- Implemented cart and account for ordering/downloading imagery; extended Leaflet with WMS cadastral data and object info.
- Enhanced GeoJSON styling (colors, borders, interactivity); virtualized table scrolling for large datasets (BackboneJS).
- Initiated regression testing: wrote test cases, hired and onboarded the first tester.
- Refactored “Satellite Imagery Catalog”: migrated ExtJS → BackboneJS; full REST integration; white‑label theming/branding/geographic restrictions.
- Integrated cartographic components into Django Admin; automated builds (Grunt), dependencies (Bower), Django integration.
- Adopted Mercurial (Hg) and Bitbucket as primary VCS.

### **undev.ru** — Frontend Developer — _Jun 2012 — Jun 2013_ — Moscow

- Built BackboneJS SPA for live broadcasts from 1,000+ polling stations (Elections 2012).
- Implemented Yandex.Maps‑based cartography with clustering; CoffeeScript video player for PEMF 2010 forum.
- SPA for archived election video browsing with time/station search; platform theming and map/data configuration for clients.
- Modular tests with MochaJS/SinonJS; build with Grunt/Bower; architecture with dependency injection (RequireJS).

### **bigbuzzy.ru** — Frontend Developer — _Mar 2011 — Jun 2012_ — Moscow

- Interfaces with HTML/CSS/jQuery/BackboneJS/XSLT; pixel‑perfect cross‑browser layout including IE 6–8.
- Integrated frontend into proprietary framework (Imprimatur engine); optimized XSLT for rendering performance.
- Authored UI guidelines and CSS component library; mentored junior specialists; dynamic AJAX banner components and comment feed improvements.
- CSS3 animations with graceful degradation; email templates for campaigns; introduced Git and formalized repo workflows.

### **JV Media (snob.ru)** — HTML/CSS/JS Developer — _Aug 2010 — Mar 2011_ — Moscow

- Pixel‑perfect cross‑browser layout; integration into PHP Zend Framework; jQuery plugins (form validation, image viewer).
- Legacy IE 6–8 adaptations; AJAX comment feed with dynamic content; SVN workflows.

### **PlatZkart LLC** — Content Manager / Frontend Developer — _Nov 2009 — Jul 2010_ — Krasnodar

- Cross‑browser layouts and integration into 1C‑Bitrix; content management and basic SEO.
- Maintained client sites; built a Tilda‑like site builder; ongoing technical support.

### **Contractstroy LLC** — System Administrator — _Jan 2008 — Aug 2009_ — Krasnodar

- Administered corporate file server; maintained Ubuntu‑based mail server (install/config/backup).
- Implemented internet traffic control (rate limiting, non‑work site filtering) and load balancing across two providers.
- Supported office IT infrastructure (~40 workstations and peripherals); maintained 1C:Enterprise 7.7–8.1; corporate website support.

## Education

**Kuban State University** — _2009_  
Faculty of Theoretical Physics (Engineer)

## Featured Links

- Geospatial platform demo (YouTube): youtu.be/df4GsBd9a_U
- GitHub — hello‑bot: github.com/ivan-hilckov/hello-bot
- GitHub — hello‑ai‑bot: github.com/ivan-hilckov/hello-ai-bot
- GitHub — english‑teacher‑bot: github.com/ivan-hilckov/english-teacher-bot
- Full CV (PDF): ./CV.pdf

## Availability & Preferences

- Remote‑first; open to hybrid; open to relocation.
- Immediate availability; open to international contract and invoicing.
