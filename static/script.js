// ---------- Dark mode ----------
const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const themeLabel = document.getElementById('themeLabel');

function applyTheme(theme) {
  root.setAttribute('data-theme', theme);
  themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
  themeLabel.textContent = theme === 'dark' ? 'Light mode' : 'Dark mode';
}

// Default to the user's system preference on load
applyTheme(window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

themeToggle.addEventListener('click', () => {
  const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  applyTheme(next);
});

// ---------- Chat area ----------
const chatForm = document.getElementById('chatForm');
const chatInput = document.getElementById('chatInput');
const chatLog = document.getElementById('chatLog');

function addChatMessage(text, sender) {
  const msg = document.createElement('div');
  msg.className = 'msg msg-' + sender;
  const p = document.createElement('p');
  p.textContent = text;
  msg.appendChild(p);
  chatLog.appendChild(msg);
  chatLog.scrollTop = chatLog.scrollHeight;
  return msg;
}

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const model=modelDropdownMenu.value;
  const text = chatInput.value.trim();
  if (!text) return;

  addChatMessage(text, 'user');
  chatInput.value = '';

  // Show a pending state while waiting for the automation backend to respond.
  const pending = addChatMessage('Looking for recipes...', 'bot');
  pending.classList.add('msg-pending');

  try {
    const response = await fetch("/", {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ model:model, ingredients: text })
    });

    const data = await response.json(); // or response.json() if Flask returns JSON
    pending.classList.remove('msg-pending');
    if (data.status === 'ok') {
  const r = data.recipe;
pending.querySelector('p').innerHTML =
  `${r.recipe_name} (${r.prep_time_minutes} min)<br>
   Ingredients: ${r.ingredients.join(', ')}<br>
   <a href="${r.youtube_search_url}" target="_blank">Watch on YouTube</a>`;
} else {
  pending.querySelector('p').textContent = data.reply;
}
  } catch (err) {
    pending.classList.remove('msg-pending');
    pending.querySelector('p').textContent = 'Something went wrong, please try again.';
    console.error(err);
  }
});

// ---------- Recipe display area ----------
const results = document.getElementById('results');
const emptyState = document.getElementById('emptyState');

function addRecipeCard({ title, time, servings, description, ingredients }) {
  emptyState.style.display = 'none';

  const card = document.createElement('div');
  card.className = 'recipe-card';

  card.innerHTML = `
    <div class="recipe-card-head">
      <h3></h3>
      <span class="recipe-meta"></span>
    </div>
    <p class="recipe-desc"></p>
    <div class="tag-list"></div>
  `;

  card.querySelector('h3').textContent = title;
  card.querySelector('.recipe-meta').textContent = [time, servings].filter(Boolean).join(' · ');
  card.querySelector('.recipe-desc').textContent = description || '';

  const tagList = card.querySelector('.tag-list');
  (ingredients || []).forEach(ing => {
    const tag = document.createElement('span');
    tag.className = 'tag';
    tag.textContent = ing;
    tagList.appendChild(tag);
  });

  results.appendChild(card);
}

// Example cards to preview the layout — remove these two lines once
// your automation backend is wired up to call addRecipeCard() itself.
addRecipeCard({ title: 'Spinach & Egg Fried Rice', time: '20 min', servings: '2 servings', description: 'A quick fried rice that uses up leftover cooked rice, eggs, and wilting greens.', ingredients: ['rice', 'eggs', 'spinach', 'soy sauce', 'garlic'] });
addRecipeCard({ title: 'Veggie Scrap Omelette', time: '12 min', servings: '1 serving', description: 'Turns odds and ends of vegetables into a full breakfast.', ingredients: ['eggs', 'onion', 'bell pepper', 'cheese'] });
