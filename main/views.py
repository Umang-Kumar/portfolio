from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.views import generic
from django.contrib import messages
from . forms import ContactForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		educations = Education.objects.filter(is_active=True)
		coding = CodingProfiles.objects.filter(is_active=True)
		latest_portfolio  = Portfolio.objects.all().order_by('-date')[0:3]
		latest_blog  = Blog.objects.all().order_by('-timestamp')[0:3]
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["latest_blog"] = latest_blog
		context["portfolio"] = portfolio
		context["latest_portfolio"] = latest_portfolio
		context["educations"] = educations
		context["coding"] = coding
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		email = self.request.POST.get('email')
        # Validate the email address
		try:
			validate_email(email)
		except ValidationError:
			messages.error(self.request, 'Please enter a valid email address.')
			return super().form_invalid(form)

        # Save the form
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')

        # Send the email
		send_mail(
            subject="Response from Umang Kumar",
            message=f"Hello! Thank you for contacting me. I'll reach out to you soon.\nThis is what I got from you:\n'{form.cleaned_data['message']}'\n\nRegards,\nUmang Kumar",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email, settings.EMAIL_PRIMARY]
        )
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		queryset = super().get_queryset().filter(is_active=True)

		latest_portfolio = Portfolio.objects.all().order_by('-date')[:3]
		latest_ids = [obj.id for obj in latest_portfolio]

		for obj in queryset:
			if obj.id in latest_ids:
				obj.is_new = True
			else:
				obj.is_new = False

		return queryset


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"
