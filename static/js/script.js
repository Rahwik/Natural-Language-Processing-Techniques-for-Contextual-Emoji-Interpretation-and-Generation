// Create a container for Three.js rendering
const container = document.createElement('div');
document.body.appendChild(container);

// Set the renderer size
const width = window.innerWidth;
const height = window.innerHeight;

const renderer = new THREE.WebGLRenderer();
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(width, height);
document.body.appendChild(renderer.domElement);

// Create a scene
const scene = new THREE.Scene();

// Create a camera
const camera = new THREE.PerspectiveCamera(45, width / height, 1, 2000);
camera.position.set(0, 0, +1000);

// Add a point light to the scene
const pointLight = new THREE.PointLight(0xFFFFFF, 2.5, 1000);
scene.add(pointLight);

// Create a group of meshes (spheres)
const group = new THREE.Group();
const geometry = new THREE.SphereGeometry(30, 32, 16);
const material = new THREE.MeshToonMaterial({ color: 0xffcc33, transparent: true, opacity: 0.8 });

for (let i = 0; i < 2000; i++) {
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(Math.random() * 2000 - 1000, Math.random() * 2000 - 1000, Math.random() * 2000 - 1000);
    mesh.rotation.set(Math.random() * 2 * Math.PI, Math.random() * 2 * Math.PI, 0);
    const scale = Math.random() * 2;
    mesh.scale.set(scale, scale, scale);
    group.add(mesh);
}

scene.add(group);

// Add fog effect to the scene
scene.fog = new THREE.FogExp2(0x000000, 0.0002);

// Animation function
function animate() {
    requestAnimationFrame(animate);
    group.rotation.x += 0.0005;
    group.rotation.y += 0.002;
    renderer.render(scene, camera);
}

animate();

// Resize event listener
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
