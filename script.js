const projects=[
  {
    id:"examforge",name:"ExamForge AI",
    screens:["examforgeai-bank.webp","examforgeai-authoring.webp","examforgeai-assessment.webp"],
    pt:["Banco de questões","Elaboração assistida","Avaliação montada"],
    en:["Question bank","Assisted authoring","Assembled assessment"]
  },
  {
    id:"clinicaltrack",name:"ClinicalTrack",
    screens:["clinicaltrack-dashboard.webp","clinicaltrack-placements.webp","clinicaltrack-evaluation.webp"],
    pt:["Visão do gestor","Placements","Avaliação formativa"],
    en:["Manager view","Placements","Formative assessment"]
  },
  {
    id:"serviceflow",name:"ServiceFlow",
    screens:["serviceflow-dashboard.webp","serviceflow-form.webp"],
    pt:["Dashboard","Novo atendimento"],
    en:["Dashboard","New service request"]
  },
  {
    id:"teammural",name:"TeamMural",
    screens:["teammural-general.webp","teammural-direct.webp"],
    pt:["Canal geral","Conversa individual"],
    en:["General channel","Direct conversation"]
  }
];

const gallery=document.getElementById("gallery");
if(gallery){
  const picture=gallery.querySelector("img");
  const tabs=gallery.querySelector(".gallery-tabs");
  const isEnglish=document.documentElement.lang.toLowerCase().startsWith("en");
  document.querySelectorAll(".open-gallery").forEach(button=>button.addEventListener("click",()=>{
    const project=projects.find(p=>p.id===button.dataset.project);
    if(!project)return;
    const labels=isEnglish?project.en:project.pt;
    document.getElementById("gallery-title").textContent=project.name;
    tabs.replaceChildren();
    function selectScreen(i){
      picture.src="screens/"+project.screens[i];
      picture.alt=project.name+" — "+labels[i]+" — "+(isEnglish?"synthetic data":"dados sintéticos");
      tabs.querySelectorAll("button").forEach((b,j)=>b.setAttribute("aria-pressed",String(i===j)));
    }
    project.screens.forEach((screen,i)=>{
      const tab=document.createElement("button");
      tab.type="button";
      tab.textContent=labels[i];
      tab.onclick=()=>selectScreen(i);
      tabs.appendChild(tab);
    });
    selectScreen(0);
    gallery.showModal();
  }));
  const close=document.getElementById("gallery-close");
  if(close)close.onclick=()=>gallery.close();
  gallery.addEventListener("click",e=>{if(e.target===gallery)gallery.close();});
}
