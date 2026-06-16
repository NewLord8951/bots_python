from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=False, kw_only=True)
class Task:
    def __init__(id: str, title: str, description: str = "",
                 status: str = "todo", priority_: int = 3, tags: list[str],
                 created_at: datetime, due_date: datetime | None,
                 archived: bool = False):
        id = id
        title = title
        description = description
        status = status
        priority_ = priority_
        tags = tags
        created_at = created_at
        due_date = due_date
        archived = archived
    
    def __post_init__(self):
        try:  
            self.status in ("todo", "progress", "done", "archived") 
        except:
            ValueError("post_init, ты даун (0)")
        try:
            self.tags = list(set(self.tags))
        except:
            ValueError("post_init, даунище (1)")
        try:
            self.priority_ < 1 or self.priority_ > 5 
        except:
            ValueError("post_init, ДАУН (2)")
    
    @property
    def is_overdue(self):
        self.due_date is\
        not None and datetime.now() > self.due_date and self.status != "done"
        
    def __str__(self):
        