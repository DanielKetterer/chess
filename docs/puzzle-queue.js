(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.PuzzleQueue=api})(this,function(){
function priorityOf(p,now=new Date()){const a=p.attemptSummary,d=p.dueAt?new Date(p.dueAt):null;if(d&&now<d)return 99;if(a.status==='failed_repeatedly')return 0;if(a.status==='unattempted')return 2;return 1}
function order(puzzles,now=new Date(),includeAll=true){return [...puzzles].map((p,index)=>({p,index,priority:priorityOf(p,now)})).filter(x=>includeAll||x.priority<99).sort((a,b)=>a.priority-b.priority||String(a.p.attemptSummary.lastAt||'').localeCompare(String(b.p.attemptSummary.lastAt||''))||a.index-b.index).map(x=>x.p)}
function selectPuzzle(puzzles,now=new Date(),includeAll=false){return order(puzzles,now,includeAll)[0]||null}
return{priorityOf,order,selectPuzzle};});
