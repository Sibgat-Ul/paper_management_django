class ThesisTopic:
    def __init__(self, t_id, title, supervisor, category):
        self.TopicNo = t_id
        self.Title = title
        self.ThesisSupervisor = supervisor
        self.Category = category


class ThesisDescription:
    def __init__(self, t_id, description):
        self.TopicNo = t_id
        self.Description = description
