from django.db import models
from charities.models import Charity
from voting.moremodels import Category
from django.contrib.auth.models import User


class STATUS(object):
    """
    Status of the team
    """
    ACTIVE = 'A'
    DISQUALIFIED = 'D'
    DELETED = 'X'

    CHOICES = (
        (ACTIVE, 'Active'),
        (DISQUALIFIED, 'Disqualified'),
        (DELETED, 'Deleted'),
    )


class TYPE(object):
    """
    Type of project -- 'implemented' (working code) or 'concept' (smoke and
    Powerpoint mirrors)
    """
    # I honestly came really close to calling these 'SMOKE' and 'MIRRORS' but
    # couldn't decide which to assign to which. - mpirnat
    IMPLEMENTED = 'I'
    CONCEPT = 'C'

    CHOICES = (
        (IMPLEMENTED, 'Implemented'),
        (CONCEPT, 'Concept'),
    )


class Team(models.Model):
    """
    A team of participants that will work on a project and compete for fabulous
    prizes, fame, and glory.

    Upon creation, a team needs:

        * a name--hopefully an awesome one
        * a slug, to be used for the URL of the team's page
        * a project description
        * a project type, so that we can differentiate "real" hacks vs. thought
          experiments (aka "code vs. ppt")
        * a creator
        * a captain
        * team members
        * a judged category
        * a charity that the team is supporting

    The creator and captain may have management powers above and beyond
    those of a mere member.
    """

    name = models.CharField('name of team', max_length=255, db_index=True,
            unique=True)
    slug = models.SlugField('slugified team name', db_index=True, unique=True)
    project = models.TextField('description of project')

    type = models.CharField('type of project', max_length=1, db_index=True,
            choices=TYPE.CHOICES)
    status = models.CharField(max_length=1, db_index=True,
            choices=STATUS.CHOICES)

    creator = models.ForeignKey(User,
            related_name="%(app_label)s_%(class)s_creator")
    captain = models.ForeignKey(User,
            related_name="%(app_label)s_%(class)s_captain")
    members = models.ManyToManyField(User,
            related_name="%(app_label)s_%(class)s_members")

    category = models.ForeignKey(Category)
    charity = models.ForeignKey(Charity)

    create_date = models.DateTimeField('date created', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)

    def __unicode__(self):
        return self.name
