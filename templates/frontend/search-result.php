{% if statuss > 0 %}
    <ul class="statuss">
        {% for status in statuss %}
            <li>
                <p>{{status}}</p>
            </li>
        {% endfor %}    
    </ul>
{% else %}
    <p>No status found.</p>
{% endif %}