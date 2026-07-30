import os
import json
from openai import OpenAI

client = OpenAI()

projects = [
    {
        "name": "PhantomBox",
        "description": "Resource-Efficient Malware Analysis Sandbox with Anti-VM detection.",
        "tech": ["Python", "QEMU", "Tiny10"],
        "color": "#39D353"
    },
    {
        "name": "Secure Voting System",
        "description": "Military-grade online voting platform with E2EE and cryptographic verification.",
        "tech": ["Python", "Flask", "PostgreSQL"],
        "color": "#58A6FF"
    },
    {
        "name": "SysInfo Forensics Tool",
        "description": "Digital forensic investigation tool for Windows registry artifacts.",
        "tech": ["Python", "Flask", "Forensics"],
        "color": "#FFD700"
    },
    {
        "name": "ZapNik Scanner",
        "description": "Unified interface orchestrating OWASP ZAP and Nikto for server assessment.",
        "tech": ["Python", "Security", "Automation"],
        "color": "#FF6B6B"
    },
    {
        "name": "LinkedIn Job Scraper",
        "description": "Automated job scraping using n8n and Apify with email alerts.",
        "tech": ["n8n", "Apify", "Automation"],
        "color": "#0077B5"
    },
    {
        "name": "Logic Bomb Monitor",
        "description": "Security testing tool monitoring public IP/location changes and internet connectivity.",
        "tech": ["Python", "Networking", "Alerting"],
        "color": "#BD93F9"
    }
]

def generate_svg(project):
    prompt = f"""
    Create a high-end, animated SVG card for a GitHub README.
    Project Name: {project['name']}
    Description: {project['description']}
    Technologies: {', '.join(project['tech'])}
    Primary Color: {project['color']}
    
    The SVG should:
    1. Have a dark theme background (#0D1117) with a subtle border.
    2. Use glassmorphism effects (translucent layers).
    3. Include a subtle animation (e.g., a glowing pulse, a moving light ray, or a floating element).
    4. Be responsive (viewBox based).
    5. Use a professional, clean font (system fonts).
    6. Include a small icon related to the project (e.g., a shield for security, a box for PhantomBox).
    
    Output ONLY the SVG code, no markdown, no explanation.
    """
    
    resp = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        extra_body={"thinking": {"type": "enabled", "budget_tokens": 1024}}
    )
    return resp.choices[0].message.content

os.makedirs("/home/ubuntu/arslanjv_profile_readme/assets", exist_ok=True)

for i, project in enumerate(projects):
    print(f"Generating SVG for {project['name']}...")
    svg_content = generate_svg(project)
    # Strip markdown code blocks if present
    if "```svg" in svg_content:
        svg_content = svg_content.split("```svg")[1].split("```")[0].strip()
    elif "```" in svg_content:
        svg_content = svg_content.split("```")[1].split("```")[0].strip()
        
    filename = f"/home/ubuntu/arslanjv_profile_readme/assets/project_{i}.svg"
    with open(filename, "w") as f:
        f.write(svg_content)
    print(f"Saved to {filename}")
